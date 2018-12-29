# Yuin PK2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.6; 96 4.4; 106 3.5; 116 2.8; 128 2.2; 141 1.7; 155 1.4; 170 1.2; 187 1.1; 206 1.1; 227 1.0; 249 1.0; 274 1.1; 302 1.2; 332 1.4; 365 1.6; 402 1.1; 442 1.1; 486 1.7; 535 1.7; 588 1.5; 647 1.3; 712 1.1; 783 0.9; 861 0.6; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -1.0; 1387 -1.9; 1526 -3.2; 1678 -4.4; 1846 -5.3; 2031 -5.7; 2234 -5.7; 2457 -4.7; 2703 -3.2; 2973 -1.2; 3270 0.4; 3597 1.0; 3957 -0.5; 4353 -2.9; 4788 -4.4; 5267 -4.6; 5793 -4.7; 6373 -2.9; 7010 -0.5; 7711 -0.8; 8482 -2.9; 9330 -3.4; 10263 -0.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.44 | 6.7 dB  |
| Peaking | 1855 Hz  | 0.37 | 3.2 dB  |
| Peaking | 1951 Hz  | 1.37 | -9.1 dB |
| Peaking | 5456 Hz  | 2.09 | -5.8 dB |
| Peaking | 21803 Hz | 1.98 | -1.2 dB |
| Peaking | 83 Hz    | 5.62 | 1.5 dB  |
| Peaking | 2506 Hz  | 5.46 | -1.3 dB |
| Peaking | 3486 Hz  | 5.65 | 2.5 dB  |
| Peaking | 9082 Hz  | 6.41 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20PK2/Yuin%20PK2.png)