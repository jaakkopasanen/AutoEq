# Periodic Audio Be
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -8.1; 23 -8.1; 25 -8.0; 28 -8.0; 31 -7.9; 34 -7.8; 37 -7.8; 41 -7.7; 45 -7.6; 49 -7.6; 54 -7.6; 60 -7.6; 66 -7.5; 72 -7.4; 79 -7.4; 87 -7.4; 96 -7.4; 106 -7.4; 116 -7.3; 128 -7.2; 141 -6.9; 155 -6.6; 170 -6.2; 187 -5.8; 206 -5.2; 227 -4.5; 249 -4.2; 274 -5.1; 302 -4.5; 332 -3.7; 365 -3.1; 402 -2.8; 442 -2.4; 486 -1.9; 535 -1.4; 588 -0.9; 647 -0.5; 712 -0.1; 783 0.2; 861 0.4; 947 0.3; 1042 -0.2; 1146 -1.0; 1261 -1.7; 1387 -2.0; 1526 -2.0; 1678 -2.0; 1846 -2.4; 2031 -2.3; 2234 -2.3; 2457 -2.2; 2703 -1.5; 2973 -0.5; 3270 0.5; 3597 1.5; 3957 2.2; 4353 2.4; 4788 1.9; 5267 0.0; 5793 -3.9; 6373 -6.1; 7010 -2.2; 7711 0.2; 8482 -0.3; 9330 -2.2; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.0; 16529 -5.9; 18182 -9.0; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.56 | -5.2 dB  |
| Peaking | 67 Hz    | 0.29 | -5.2 dB  |
| Peaking | 158 Hz   | 0.46 | -2.4 dB  |
| Peaking | 6271 Hz  | 7.52 | -6.9 dB  |
| Peaking | 18654 Hz | 1.44 | -10.4 dB |
| Peaking | 857 Hz   | 1.44 | 2.7 dB   |
| Peaking | 2782 Hz  | 0.43 | -4.3 dB  |
| Peaking | 4217 Hz  | 1.14 | 6.6 dB   |
| Peaking | 5742 Hz  | 6.56 | -2.4 dB  |
| Peaking | 13179 Hz | 2.8  | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)