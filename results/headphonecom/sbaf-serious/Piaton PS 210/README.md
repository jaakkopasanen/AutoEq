# Piaton PS 210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.4; 54 4.9; 60 4.2; 66 3.6; 72 3.0; 79 2.4; 87 1.9; 96 1.4; 106 0.9; 116 0.5; 128 0.0; 141 -0.4; 155 -0.7; 170 -1.1; 187 -1.3; 206 -1.6; 227 -1.7; 249 -1.9; 274 -1.9; 302 -1.8; 332 -1.9; 365 -1.9; 402 -1.9; 442 -2.2; 486 -1.9; 535 -1.7; 588 -1.7; 647 -1.7; 712 -1.8; 783 -1.4; 861 -1.0; 947 -0.4; 1042 0.2; 1146 0.9; 1261 1.3; 1387 1.5; 1526 1.2; 1678 0.6; 1846 -0.5; 2031 -2.0; 2234 -3.7; 2457 -4.0; 2703 -1.0; 2973 2.8; 3270 5.9; 3597 6.0; 3957 4.7; 4353 1.1; 4788 1.6; 5267 5.6; 5793 4.7; 6373 0.6; 7010 -1.1; 7711 -5.9; 8482 -6.5; 9330 -0.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Piaton PS 210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.85 | 7.0 dB  |
| Peaking | 2399 Hz |  4.11 | -5.9 dB |
| Peaking | 3421 Hz |  3.11 | 7.2 dB  |
| Peaking | 5524 Hz |  5.96 | 6.3 dB  |
| Peaking | 8076 Hz |  5.2  | -8.3 dB |
| Peaking | 72 Hz   |  1.22 | 1.4 dB  |
| Peaking | 376 Hz  |  0.34 | -2.2 dB |
| Peaking | 1322 Hz |  2.05 | 2.7 dB  |
| Peaking | 4533 Hz | 12.23 | -1.7 dB |
| Peaking | 9681 Hz |  9.06 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Piaton%20PS%20210/Piaton%20PS%20210.png)