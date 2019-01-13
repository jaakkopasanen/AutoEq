# NAD VISO HP50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -6.4; 23 -6.4; 25 -6.3; 28 -6.2; 31 -6.1; 34 -6.0; 37 -5.8; 41 -5.6; 45 -5.5; 49 -5.3; 54 -5.1; 60 -4.9; 66 -4.7; 72 -4.4; 79 -4.2; 87 -3.9; 96 -3.4; 106 -3.1; 116 -3.6; 128 -5.4; 141 -6.4; 155 -5.5; 170 -4.2; 187 -5.4; 206 -5.6; 227 -5.2; 249 -4.6; 274 -3.9; 302 -3.1; 332 -2.1; 365 -2.1; 402 -1.6; 442 -1.3; 486 -1.2; 535 -0.9; 588 -0.4; 647 -0.1; 712 -0.0; 783 -0.5; 861 -0.8; 947 -0.5; 1042 -0.2; 1146 -0.6; 1261 -1.9; 1387 -3.1; 1526 -3.8; 1678 -3.6; 1846 -2.3; 2031 -1.6; 2234 -0.5; 2457 0.8; 2703 2.2; 2973 2.9; 3270 2.6; 3597 2.0; 3957 0.7; 4353 -1.9; 4788 -2.7; 5267 0.6; 5793 2.5; 6373 3.4; 7010 2.0; 7711 0.3; 8482 -1.2; 9330 -1.6; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1    | -4.4 dB |
| Peaking | 46 Hz   | 0.74 | -4.0 dB |
| Peaking | 186 Hz  | 0.92 | -5.2 dB |
| Peaking | 1561 Hz | 3.73 | -4.3 dB |
| Peaking | 103 Hz  | 7.39 | 0.7 dB  |
| Peaking | 3132 Hz | 3.02 | 3.4 dB  |
| Peaking | 4721 Hz | 4.64 | -4.6 dB |
| Peaking | 6152 Hz | 2.43 | 3.9 dB  |
| Peaking | 8821 Hz | 3.84 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)