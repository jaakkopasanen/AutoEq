# Sony MDR-7502
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 5.2; 155 4.2; 170 4.4; 187 3.6; 206 3.4; 227 3.0; 249 2.8; 274 2.7; 302 2.8; 332 3.0; 365 2.5; 402 2.4; 442 2.0; 486 1.3; 535 1.1; 588 1.4; 647 1.3; 712 1.1; 783 1.0; 861 0.5; 947 0.1; 1042 -0.2; 1146 -0.8; 1261 -1.4; 1387 -1.7; 1526 -2.5; 1678 -3.5; 1846 -3.6; 2031 -3.3; 2234 -2.9; 2457 -1.3; 2703 0.1; 2973 1.5; 3270 2.4; 3597 3.1; 3957 4.4; 4353 5.2; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -2.5; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7502 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7502 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.09 | 5.7 dB  |
| Peaking | 182 Hz  | 0.24 | 1.6 dB  |
| Peaking | 1910 Hz | 1.37 | -5.3 dB |
| Peaking | 5627 Hz | 0.84 | 8.4 dB  |
| Peaking | 8552 Hz | 1.47 | -5.9 dB |
| Peaking | 121 Hz  | 1.8  | 1.6 dB  |
| Peaking | 223 Hz  | 0.4  | -1.1 dB |
| Peaking | 356 Hz  | 1.58 | 1.2 dB  |
| Peaking | 511 Hz  | 5.81 | -0.6 dB |
| Peaking | 695 Hz  | 2.06 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7502/Sony%20MDR-7502.png)