# Sony MDR-D77 Eggo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.2; 49 4.4; 54 3.7; 60 3.1; 66 2.6; 72 2.2; 79 1.8; 87 1.5; 96 1.2; 106 1.1; 116 1.3; 128 1.5; 141 1.3; 155 1.1; 170 1.4; 187 1.5; 206 1.5; 227 2.1; 249 2.5; 274 2.7; 302 3.4; 332 3.4; 365 2.6; 402 3.3; 442 3.4; 486 2.7; 535 2.0; 588 1.5; 647 0.9; 712 0.5; 783 0.5; 861 0.1; 947 0.1; 1042 -0.3; 1146 -0.4; 1261 0.9; 1387 2.3; 1526 0.1; 1678 -1.5; 1846 -1.8; 2031 -1.2; 2234 -0.1; 2457 1.8; 2703 3.1; 2973 4.8; 3270 5.7; 3597 4.7; 3957 4.3; 4353 5.3; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-D77 Eggo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-D77 Eggo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.69 | 6.5 dB  |
| Peaking | 354 Hz  | 1.09 | 3.4 dB  |
| Peaking | 1922 Hz | 3.56 | -3.1 dB |
| Peaking | 3216 Hz | 2.04 | 4.8 dB  |
| Peaking | 5408 Hz | 2.26 | 6.0 dB  |
| Peaking | 462 Hz  | 6.76 | 0.7 dB  |
| Peaking | 1220 Hz | 1.61 | -1.3 dB |
| Peaking | 1369 Hz | 6.17 | 3.5 dB  |
| Peaking | 6506 Hz | 6.83 | 2.5 dB  |
| Peaking | 7966 Hz | 2.09 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-D77%20Eggo/Sony%20MDR-D77%20Eggo.png)