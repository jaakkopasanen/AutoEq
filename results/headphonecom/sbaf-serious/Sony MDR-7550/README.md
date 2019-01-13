# Sony MDR-7550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.5; 28 3.2; 31 3.0; 34 2.8; 37 2.6; 41 2.4; 45 2.1; 49 1.9; 54 1.7; 60 1.2; 66 0.8; 72 0.6; 79 0.2; 87 -0.1; 96 -0.4; 106 -0.6; 116 -0.9; 128 -1.2; 141 -1.5; 155 -1.7; 170 -1.9; 187 -2.0; 206 -2.1; 227 -2.1; 249 -1.9; 274 -1.9; 302 -1.8; 332 -1.4; 365 -1.3; 402 -0.9; 442 -0.8; 486 -0.5; 535 -0.4; 588 -0.1; 647 0.3; 712 0.5; 783 0.4; 861 0.3; 947 0.0; 1042 0.2; 1146 -0.3; 1261 -1.5; 1387 -2.5; 1526 -3.5; 1678 -4.0; 1846 -3.8; 2031 -3.1; 2234 -1.6; 2457 0.5; 2703 3.0; 2973 5.6; 3270 6.0; 3597 6.0; 3957 5.9; 4353 2.5; 4788 -1.9; 5267 -1.7; 5793 4.5; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.49 | 3.9 dB  |
| Peaking | 195 Hz  | 0.88 | -2.4 dB |
| Peaking | 1792 Hz | 2.23 | -5.1 dB |
| Peaking | 3300 Hz | 2.61 | 7.5 dB  |
| Peaking | 6288 Hz | 7.18 | 6.0 dB  |
| Peaking | 864 Hz  | 1.63 | 0.9 dB  |
| Peaking | 1416 Hz | 5.58 | -1.0 dB |
| Peaking | 4039 Hz | 7.47 | 3.4 dB  |
| Peaking | 5025 Hz | 4.9  | -5.4 dB |
| Peaking | 5746 Hz | 7.95 | 3.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)