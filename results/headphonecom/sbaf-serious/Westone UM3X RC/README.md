# Westone UM3X RC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.6; 28 1.2; 31 0.9; 34 0.6; 37 0.4; 41 0.1; 45 -0.1; 49 -0.4; 54 -0.7; 60 -1.2; 66 -1.5; 72 -1.7; 79 -2.2; 87 -2.6; 96 -2.9; 106 -3.2; 116 -3.4; 128 -3.7; 141 -3.7; 155 -4.0; 170 -4.2; 187 -4.1; 206 -4.1; 227 -4.0; 249 -3.9; 274 -3.8; 302 -3.5; 332 -3.1; 365 -2.7; 402 -2.3; 442 -2.0; 486 -1.6; 535 -1.1; 588 -0.6; 647 -0.2; 712 0.1; 783 0.4; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.1; 1526 -1.6; 1678 -1.6; 1846 -0.6; 2031 0.8; 2234 2.7; 2457 5.1; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -2.9; 10263 -2.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM3X RC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.56 | 2.8 dB  |
| Peaking | 192 Hz   | 0.42 | -4.4 dB |
| Peaking | 1628 Hz  | 1.32 | -7.9 dB |
| Peaking | 3088 Hz  | 0.39 | 8.3 dB  |
| Peaking | 9400 Hz  | 2.05 | -6.0 dB |
| Peaking | 2601 Hz  | 7.42 | 1.4 dB  |
| Peaking | 4242 Hz  | 1.26 | -1.2 dB |
| Peaking | 6654 Hz  | 1.64 | 2.6 dB  |
| Peaking | 7371 Hz  | 5.3  | -3.4 dB |
| Peaking | 15107 Hz | 1.43 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)