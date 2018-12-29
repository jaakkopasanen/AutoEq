# Sony MDR-XB500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.0; 23 -5.5; 25 -5.9; 28 -6.3; 31 -6.7; 34 -6.9; 37 -7.1; 41 -7.4; 45 -7.6; 49 -7.8; 54 -7.9; 60 -7.8; 66 -7.8; 72 -8.1; 79 -8.7; 87 -9.2; 96 -9.4; 106 -10.2; 116 -10.7; 128 -11.3; 141 -12.0; 155 -12.3; 170 -12.2; 187 -12.5; 206 -12.8; 227 -13.1; 249 -12.9; 274 -12.2; 302 -11.8; 332 -11.0; 365 -10.1; 402 -9.5; 442 -8.6; 486 -7.6; 535 -6.3; 588 -4.5; 647 -2.9; 712 -1.4; 783 0.1; 861 0.9; 947 0.5; 1042 -0.1; 1146 -1.1; 1261 -3.0; 1387 -4.6; 1526 -5.4; 1678 -5.4; 1846 -4.9; 2031 -3.9; 2234 -2.6; 2457 -0.8; 2703 1.4; 2973 3.5; 3270 5.7; 3597 6.0; 3957 4.1; 4353 0.2; 4788 -4.0; 5267 -4.7; 5793 -2.9; 6373 -1.8; 7010 -0.2; 7711 0.3; 8482 0.0; 9330 -0.4; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 0.28 | -7.0 dB |
| Peaking | 203 Hz  | 0.86 | -8.7 dB |
| Peaking | 379 Hz  | 1.66 | -5.1 dB |
| Peaking | 1709 Hz | 2.5  | -5.9 dB |
| Peaking | 3397 Hz | 4.52 | 7.6 dB  |
| Peaking | 530 Hz  | 3.77 | -1.8 dB |
| Peaking | 871 Hz  | 2.12 | 3.1 dB  |
| Peaking | 1364 Hz | 5.75 | -2.1 dB |
| Peaking | 3846 Hz | 6.57 | 3.3 dB  |
| Peaking | 5107 Hz | 3.66 | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB500/Sony%20MDR-XB500.png)