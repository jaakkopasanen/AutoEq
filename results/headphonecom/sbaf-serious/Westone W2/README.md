# Westone W2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.6; 28 1.5; 31 1.5; 34 1.4; 37 1.3; 41 1.0; 45 0.9; 49 0.7; 54 0.5; 60 0.2; 66 -0.1; 72 -0.4; 79 -0.7; 87 -1.2; 96 -1.5; 106 -1.8; 116 -2.0; 128 -2.1; 141 -2.4; 155 -2.6; 170 -2.8; 187 -2.9; 206 -3.0; 227 -2.9; 249 -2.8; 274 -2.8; 302 -2.5; 332 -2.4; 365 -2.0; 402 -1.8; 442 -1.5; 486 -1.1; 535 -0.7; 588 -0.3; 647 0.1; 712 0.5; 783 0.7; 861 0.6; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.3; 1526 -2.0; 1678 -2.4; 1846 -2.4; 2031 -2.3; 2234 -1.4; 2457 0.4; 2703 3.1; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.9; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.36 | 1.9 dB  |
| Peaking | 196 Hz  | 0.45 | -3.2 dB |
| Peaking | 749 Hz  | 1.61 | 1.6 dB  |
| Peaking | 1961 Hz | 1.5  | -5.8 dB |
| Peaking | 3706 Hz | 0.9  | 7.9 dB  |
| Peaking | 2972 Hz | 7.71 | 1.9 dB  |
| Peaking | 3874 Hz | 3.82 | -0.7 dB |
| Peaking | 6311 Hz | 2.4  | 5.0 dB  |
| Peaking | 6954 Hz | 0.67 | -1.5 dB |
| Peaking | 7485 Hz | 2.76 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20W2/Westone%20W2.png)