# Panasonic RP-HC56

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.3; 28 5.1; 31 4.9; 34 4.8; 37 4.7; 41 4.6; 45 4.6; 49 4.6; 54 4.5; 60 4.3; 66 4.1; 72 4.0; 79 3.9; 87 3.6; 96 3.5; 106 3.2; 116 3.0; 128 2.8; 141 2.7; 155 2.7; 170 2.8; 187 2.7; 206 2.7; 227 2.6; 249 2.5; 274 2.2; 302 1.7; 332 1.1; 365 0.3; 402 -0.7; 442 -1.6; 486 -2.7; 535 -3.6; 588 -3.9; 647 -3.5; 712 -2.4; 783 -1.0; 861 0.2; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 0.1; 1387 0.6; 1526 1.4; 1678 2.4; 1846 3.3; 2031 4.2; 2234 5.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.3; 3957 5.2; 4353 4.9; 4788 4.2; 5267 1.1; 5793 -1.5; 6373 -1.1; 7010 0.1; 7711 -1.7; 8482 -6.5; 9330 -10.3; 10263 -11.4; 11289 -9.3; 12418 -7.1; 13660 -6.3; 15026 -3.5; 16529 -2.5; 18182 -2.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC56 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC56 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.37 | 4.8 dB   |
| Peaking | 106 Hz   | 0.22 | 3.0 dB   |
| Peaking | 571 Hz   | 1.48 | -5.6 dB  |
| Peaking | 3256 Hz  | 0.84 | 7.1 dB   |
| Peaking | 10496 Hz | 1.32 | -12.0 dB |
| Peaking | 1230 Hz  | 4.89 | -1.5 dB  |
| Peaking | 2129 Hz  | 3.66 | -0.3 dB  |
| Peaking | 5874 Hz  | 7.13 | -2.6 dB  |
| Peaking | 7307 Hz  | 6.26 | 3.2 dB   |
| Peaking | 17523 Hz | 3.54 | -1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC56/Panasonic%20RP-HC56.png)