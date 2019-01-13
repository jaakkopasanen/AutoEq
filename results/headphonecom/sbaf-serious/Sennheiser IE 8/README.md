# Sennheiser IE 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -2.3; 23 -2.9; 25 -3.5; 28 -4.1; 31 -4.7; 34 -5.3; 37 -5.7; 41 -6.3; 45 -6.8; 49 -7.2; 54 -7.7; 60 -8.2; 66 -8.7; 72 -9.2; 79 -9.5; 87 -9.9; 96 -10.4; 106 -10.4; 116 -10.6; 128 -10.8; 141 -11.0; 155 -10.9; 170 -10.9; 187 -10.6; 206 -10.3; 227 -10.0; 249 -9.5; 274 -9.0; 302 -8.3; 332 -7.5; 365 -6.6; 402 -5.9; 442 -5.3; 486 -4.6; 535 -3.7; 588 -2.8; 647 -2.0; 712 -1.3; 783 -0.7; 861 -0.3; 947 -0.3; 1042 0.1; 1146 -0.3; 1261 -0.9; 1387 -1.9; 1526 -3.0; 1678 -3.6; 1846 -3.7; 2031 -3.5; 2234 -3.1; 2457 -2.4; 2703 -1.4; 2973 -0.2; 3270 1.1; 3597 1.3; 3957 -0.3; 4353 -1.3; 4788 1.3; 5267 3.7; 5793 3.0; 6373 1.2; 7010 1.8; 7711 0.3; 8482 0.0; 9330 -0.6; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.45 | -7.9 dB |
| Peaking | 180 Hz  | 0.85 | -5.5 dB |
| Peaking | 334 Hz  | 1.25 | -3.4 dB |
| Peaking | 1897 Hz | 2.36 | -4.0 dB |
| Peaking | 5498 Hz | 4.48 | 4.1 dB  |
| Peaking | 508 Hz  | 4.12 | -0.9 dB |
| Peaking | 990 Hz  | 1.63 | 1.3 dB  |
| Peaking | 1497 Hz | 4.4  | -1.2 dB |
| Peaking | 3444 Hz | 6.55 | 2.0 dB  |
| Peaking | 4269 Hz | 8.64 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20IE%208/Sennheiser%20IE%208.png)