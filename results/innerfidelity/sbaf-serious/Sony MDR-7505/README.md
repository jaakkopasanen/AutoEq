# Sony MDR-7505
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.9; 96 5.0; 106 4.4; 116 4.4; 128 4.5; 141 3.6; 155 2.8; 170 2.9; 187 2.6; 206 2.6; 227 2.6; 249 2.6; 274 3.0; 302 2.7; 332 2.3; 365 1.7; 402 1.7; 442 1.7; 486 0.9; 535 0.4; 588 0.3; 647 -0.3; 712 -0.2; 783 1.5; 861 0.5; 947 -0.0; 1042 0.0; 1146 0.6; 1261 0.9; 1387 1.3; 1526 1.6; 1678 2.3; 1846 2.8; 2031 3.3; 2234 3.5; 2457 3.6; 2703 4.1; 2973 3.1; 3270 2.7; 3597 2.6; 3957 2.7; 4353 1.9; 4788 2.9; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7505 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.16 | 5.8 dB  |
| Peaking | 86 Hz   | 0.75 | 2.3 dB  |
| Peaking | 293 Hz  | 1.79 | 1.9 dB  |
| Peaking | 2453 Hz | 1.28 | 3.8 dB  |
| Peaking | 5786 Hz | 3.24 | 6.2 dB  |
| Peaking | 678 Hz  | 4.27 | -2.6 dB |
| Peaking | 780 Hz  | 2.24 | 2.5 dB  |
| Peaking | 934 Hz  | 3.3  | -1.9 dB |
| Peaking | 8240 Hz | 4.58 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)