# Skullcandy Venue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.5dB
GraphicEQ: 21 -12.6; 23 -12.3; 25 -12.1; 28 -11.6; 31 -11.1; 34 -10.6; 37 -10.1; 41 -9.5; 45 -9.0; 49 -8.5; 54 -8.1; 60 -7.7; 66 -7.5; 72 -7.3; 79 -7.2; 87 -7.1; 96 -7.1; 106 -7.2; 116 -7.3; 128 -7.4; 141 -7.5; 155 -7.5; 170 -7.6; 187 -7.5; 206 -7.2; 227 -6.9; 249 -6.4; 274 -5.9; 302 -5.3; 332 -4.7; 365 -3.7; 402 -2.6; 442 -1.7; 486 -1.2; 535 -0.9; 588 -0.5; 647 -0.1; 712 0.2; 783 0.4; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.7; 1261 -1.8; 1387 -3.9; 1526 -5.8; 1678 -6.8; 1846 -5.8; 2031 -5.0; 2234 -4.6; 2457 -3.9; 2703 -4.0; 2973 -5.6; 3270 -7.2; 3597 -5.8; 3957 -6.6; 4353 -6.2; 4788 -5.5; 5267 -3.6; 5793 -7.0; 6373 -9.9; 7010 -9.1; 7711 -8.1; 8482 -8.9; 9330 -10.3; 10263 -9.8; 11289 -7.8; 12418 -7.4; 13660 -10.7; 15026 -13.9; 16529 -11.9; 18182 -7.6; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Venue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-4**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Venue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.17 | -12.9 dB |
| Peaking | 192 Hz   | 0.91 | -6.1 dB  |
| Peaking | 1697 Hz  | 3.32 | -5.2 dB  |
| Peaking | 6972 Hz  | 0.45 | -7.2 dB  |
| Peaking | 16091 Hz | 1.02 | -10.7 dB |
| Peaking | 831 Hz   | 1.77 | 1.9 dB   |
| Peaking | 3239 Hz  | 8.12 | -2.0 dB  |
| Peaking | 5234 Hz  | 6.41 | 4.9 dB   |
| Peaking | 8712 Hz  | 0.4  | -1.2 dB  |
| Peaking | 12202 Hz | 4.36 | 3.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Venue/Skullcandy%20Venue.png)