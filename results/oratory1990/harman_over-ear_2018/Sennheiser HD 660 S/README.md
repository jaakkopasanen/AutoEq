# Sennheiser HD 660 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.4; 41 4.7; 45 4.2; 49 3.7; 54 3.2; 60 2.8; 66 2.2; 72 1.9; 79 2.4; 87 1.9; 96 0.7; 106 0.2; 116 -0.3; 128 -0.7; 141 -1.3; 155 -1.7; 170 -2.0; 187 -1.9; 206 -2.1; 227 -2.1; 249 -2.1; 274 -1.9; 302 -1.6; 332 -1.1; 365 -0.7; 402 -0.4; 442 -0.4; 486 -0.2; 535 0.1; 588 0.3; 647 0.4; 712 0.2; 783 -0.2; 861 -0.3; 947 0.2; 1042 -0.4; 1146 -0.6; 1261 -0.6; 1387 -0.1; 1526 1.0; 1678 2.0; 1846 3.0; 2031 4.1; 2234 4.3; 2457 3.5; 2703 2.6; 2973 1.9; 3270 1.5; 3597 1.4; 3957 2.0; 4353 3.4; 4788 3.7; 5267 -1.3; 5793 -0.4; 6373 4.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 660 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 660 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.43 | 6.2 dB  |
| Peaking | 192 Hz   | 0.95 | -2.8 dB |
| Peaking | 2284 Hz  | 1.73 | 4.2 dB  |
| Peaking | 6555 Hz  | 7.6  | 5.0 dB  |
| Peaking | 22050 Hz | 2.27 | 1.1 dB  |
| Peaking | 628 Hz   | 1.94 | 0.9 dB  |
| Peaking | 1670 Hz  | 0.93 | -2.7 dB |
| Peaking | 1837 Hz  | 1.92 | 3.1 dB  |
| Peaking | 4641 Hz  | 4.31 | 4.8 dB  |
| Peaking | 5362 Hz  | 6.57 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20660%20S/Sennheiser%20HD%20660%20S.png)