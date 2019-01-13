# Sony MDR-V6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 5.1; 45 4.4; 49 3.9; 54 3.3; 60 2.6; 66 2.5; 72 2.8; 79 2.6; 87 2.0; 96 1.6; 106 1.4; 116 1.3; 128 1.3; 141 1.3; 155 1.4; 170 1.6; 187 1.9; 206 2.0; 227 1.4; 249 0.2; 274 0.5; 302 0.9; 332 0.7; 365 0.1; 402 -0.7; 442 -0.9; 486 -1.0; 535 -1.2; 588 -0.9; 647 -0.8; 712 -0.6; 783 -0.4; 861 -0.3; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.9; 1387 -1.0; 1526 -2.0; 1678 -2.6; 1846 -2.7; 2031 -2.7; 2234 -3.2; 2457 -3.2; 2703 -4.4; 2973 -5.1; 3270 -5.0; 3597 -4.2; 3957 -3.1; 4353 -5.4; 4788 -5.0; 5267 -0.3; 5793 4.1; 6373 3.9; 7010 0.6; 7711 -1.2; 8482 -3.8; 9330 -7.1; 10263 -6.4; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.21 | 6.6 dB  |
| Peaking | 2963 Hz  | 1    | -4.6 dB |
| Peaking | 4673 Hz  | 4.82 | -4.9 dB |
| Peaking | 5983 Hz  | 3.48 | 7.2 dB  |
| Peaking | 9545 Hz  | 4.02 | -8.2 dB |
| Peaking | 62 Hz    | 3.18 | -0.9 dB |
| Peaking | 200 Hz   | 3.29 | 1.5 dB  |
| Peaking | 519 Hz   | 2.47 | -1.3 dB |
| Peaking | 1023 Hz  | 4.24 | 0.8 dB  |
| Peaking | 11636 Hz | 6.99 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)