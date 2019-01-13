# Sony MDR-7505
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.7; 116 4.6; 128 3.7; 141 3.0; 155 2.4; 170 2.1; 187 1.6; 206 1.5; 227 2.0; 249 2.7; 274 2.8; 302 2.4; 332 1.3; 365 -0.0; 402 0.2; 442 0.5; 486 0.5; 535 0.4; 588 0.3; 647 -0.0; 712 0.8; 783 1.3; 861 0.7; 947 -0.1; 1042 0.3; 1146 0.7; 1261 0.3; 1387 -0.2; 1526 -0.7; 1678 -0.2; 1846 0.3; 2031 0.7; 2234 1.0; 2457 1.2; 2703 2.1; 2973 1.1; 3270 0.7; 3597 0.6; 3957 0.5; 4353 -0.2; 4788 0.6; 5267 2.4; 5793 2.0; 6373 0.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7505 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.25 | 6.1 dB  |
| Peaking | 94 Hz    | 2.64 | 1.8 dB  |
| Peaking | 782 Hz   | 7.27 | 1.2 dB  |
| Peaking | 2659 Hz  | 3.98 | 1.8 dB  |
| Peaking | 5853 Hz  | 2.47 | 2.1 dB  |
| Peaking | 200 Hz   | 2.07 | -1.2 dB |
| Peaking | 244 Hz   | 3.33 | 1.0 dB  |
| Peaking | 290 Hz   | 2.93 | 1.6 dB  |
| Peaking | 367 Hz   | 4.54 | -1.3 dB |
| Peaking | 21582 Hz | 1.73 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)