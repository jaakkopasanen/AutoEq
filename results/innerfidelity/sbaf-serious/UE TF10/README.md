# UE TF10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.0; 25 -0.1; 28 -0.2; 31 -0.3; 34 -0.4; 37 -0.5; 41 -0.6; 45 -0.8; 49 -0.9; 54 -1.1; 60 -1.4; 66 -1.7; 72 -2.0; 79 -2.4; 87 -2.7; 96 -3.1; 106 -3.3; 116 -3.5; 128 -3.7; 141 -3.8; 155 -3.9; 170 -4.0; 187 -3.9; 206 -3.8; 227 -3.6; 249 -3.4; 274 -3.1; 302 -2.8; 332 -2.6; 365 -2.3; 402 -2.0; 442 -1.5; 486 -1.3; 535 -1.0; 588 -0.4; 647 -0.1; 712 0.0; 783 0.3; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.1; 1261 -0.1; 1387 -0.3; 1526 -0.3; 1678 -0.0; 1846 0.8; 2031 1.7; 2234 2.6; 2457 4.0; 2703 5.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`UE TF10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `UE TF10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 3 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 98 Hz   | 1.05 | -1.3 dB |
| Peaking | 196 Hz  | 0.64 | -3.5 dB |
| Peaking | 4009 Hz | 1.01 | 7.0 dB  |
| Peaking | 1597 Hz | 2.82 | -1.5 dB |
| Peaking | 2753 Hz | 4.09 | 2.1 dB  |
| Peaking | 4041 Hz | 3.02 | -1.3 dB |
| Peaking | 6310 Hz | 2.45 | 4.7 dB  |
| Peaking | 7308 Hz | 1.53 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/UE%20TF10/UE%20TF10.png)