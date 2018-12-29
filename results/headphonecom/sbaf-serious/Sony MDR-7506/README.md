# Sony MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.4; 54 4.5; 60 3.8; 66 3.9; 72 4.0; 79 3.4; 87 3.0; 96 2.7; 106 2.5; 116 2.5; 128 2.4; 141 2.6; 155 2.6; 170 2.8; 187 2.9; 206 3.1; 227 3.0; 249 2.6; 274 1.7; 302 1.2; 332 0.1; 365 -0.8; 402 -1.7; 442 -2.0; 486 -2.4; 535 -2.4; 588 -1.8; 647 -1.4; 712 -1.4; 783 -1.2; 861 -0.8; 947 -0.1; 1042 -0.0; 1146 -0.1; 1261 -0.3; 1387 -0.9; 1526 -1.5; 1678 -1.7; 1846 -1.5; 2031 -1.2; 2234 -1.3; 2457 -1.1; 2703 -1.8; 2973 -2.4; 3270 -1.8; 3597 -1.1; 3957 -0.3; 4353 -3.3; 4788 -4.0; 5267 0.3; 5793 5.1; 6373 3.0; 7010 -0.3; 7711 -0.2; 8482 -1.9; 9330 -5.5; 10263 -5.0; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.3  | 6.2 dB  |
| Peaking | 210 Hz  | 1.63 | 3.7 dB  |
| Peaking | 1051 Hz | 0.11 | -1.6 dB |
| Peaking | 5953 Hz | 7.02 | 7.3 dB  |
| Peaking | 9665 Hz | 5.51 | -6.1 dB |
| Peaking | 486 Hz  | 2.95 | -1.6 dB |
| Peaking | 1061 Hz | 2.68 | 1.7 dB  |
| Peaking | 3147 Hz | 3.12 | -2.3 dB |
| Peaking | 4207 Hz | 1.56 | 3.5 dB  |
| Peaking | 4625 Hz | 4.8  | -6.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7506/Sony%20MDR-7506.png)