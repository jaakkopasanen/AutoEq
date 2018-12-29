# Massdrop x Sennheiser PC37X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.8; 66 5.1; 72 4.6; 79 4.0; 87 3.9; 96 3.1; 106 2.3; 116 1.2; 128 0.5; 141 -0.1; 155 -0.6; 170 -0.9; 187 -1.0; 206 -1.1; 227 -1.2; 249 -1.1; 274 -0.8; 302 -0.7; 332 -0.6; 365 -0.4; 402 -0.4; 442 -0.3; 486 -0.2; 535 -0.1; 588 0.1; 647 0.5; 712 0.4; 783 0.2; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 0.0; 1387 0.9; 1526 1.7; 1678 1.5; 1846 0.8; 2031 0.0; 2234 0.3; 2457 0.8; 2703 0.9; 2973 0.3; 3270 1.7; 3597 4.1; 3957 4.9; 4353 3.1; 4788 -0.2; 5267 0.1; 5793 -1.2; 6373 1.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.5; 16529 -3.8; 18182 -5.1; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser PC37X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser PC37X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.67 | 7.0 dB  |
| Peaking | 731 Hz   | 2.82 | 0.2 dB  |
| Peaking | 3864 Hz  | 4.39 | 5.5 dB  |
| Peaking | 14885 Hz | 0.97 | 2.7 dB  |
| Peaking | 17809 Hz | 1.01 | -6.8 dB |
| Peaking | 86 Hz    | 1.66 | 1.8 dB  |
| Peaking | 178 Hz   | 0.89 | -2.0 dB |
| Peaking | 1590 Hz  | 4.78 | 1.8 dB  |
| Peaking | 6112 Hz  | 3.17 | -2.5 dB |
| Peaking | 6713 Hz  | 6.82 | 5.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Sennheiser%20PC37X/Massdrop%20x%20Sennheiser%20PC37X.png)