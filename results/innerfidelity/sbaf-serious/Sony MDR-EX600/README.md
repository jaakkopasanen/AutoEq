# Sony MDR-EX600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.5; 31 5.2; 34 5.0; 37 4.7; 41 4.4; 45 4.1; 49 3.9; 54 3.5; 60 3.2; 66 2.7; 72 2.4; 79 2.0; 87 1.5; 96 0.9; 106 0.6; 116 0.4; 128 0.0; 141 -0.3; 155 -0.5; 170 -0.7; 187 -0.9; 206 -1.0; 227 -1.1; 249 -1.1; 274 -1.0; 302 -0.9; 332 -0.8; 365 -0.6; 402 -0.6; 442 -0.3; 486 -0.2; 535 0.0; 588 0.6; 647 0.8; 712 0.8; 783 1.0; 861 0.7; 947 0.4; 1042 -0.1; 1146 -0.6; 1261 -1.1; 1387 -1.9; 1526 -2.7; 1678 -3.1; 1846 -2.8; 2031 -1.8; 2234 -0.3; 2457 2.2; 2703 4.3; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.2; 4788 0.2; 5267 -4.1; 5793 -0.5; 6373 4.0; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -0.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.03 | 5.9 dB  |
| Peaking | 54 Hz    | 1.63 | 2.5 dB  |
| Peaking | 1760 Hz  | 2.24 | -4.4 dB |
| Peaking | 3258 Hz  | 1.97 | 7.4 dB  |
| Peaking | 22050 Hz | 2.29 | 1.2 dB  |
| Peaking | 243 Hz   | 1.16 | -1.3 dB |
| Peaking | 748 Hz   | 2.49 | 1.3 dB  |
| Peaking | 4172 Hz  | 5.93 | 3.3 dB  |
| Peaking | 5294 Hz  | 4.35 | -6.6 dB |
| Peaking | 6394 Hz  | 5.55 | 5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX600/Sony%20MDR-EX600.png)