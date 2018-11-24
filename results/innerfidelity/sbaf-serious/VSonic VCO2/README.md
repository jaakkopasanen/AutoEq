# VSonic VCO2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 4.2; 28 4.1; 31 4.1; 34 4.0; 37 3.9; 41 3.8; 45 3.7; 49 3.5; 54 3.3; 60 3.0; 66 2.8; 72 2.5; 79 2.1; 87 1.7; 96 1.5; 106 1.2; 116 0.9; 128 0.7; 141 0.3; 155 0.1; 170 0.0; 187 -0.0; 206 -0.2; 227 -0.1; 249 -0.2; 274 -0.1; 302 -0.1; 332 -0.0; 365 0.1; 402 0.1; 442 0.5; 486 0.4; 535 0.5; 588 0.9; 647 1.0; 712 1.0; 783 1.0; 861 0.7; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.2; 1387 -1.8; 1526 -2.3; 1678 -2.5; 1846 -1.9; 2031 0.1; 2234 1.3; 2457 2.9; 2703 5.5; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.0; 4788 3.0; 5267 2.8; 5793 1.5; 6373 -1.8; 7010 -4.0; 7711 -2.3; 8482 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VCO2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VCO2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.73 | 4.1 dB  |
| Peaking | 58 Hz    | 1.24 | 1.9 dB  |
| Peaking | 1773 Hz  | 1.3  | -8.8 dB |
| Peaking | 2833 Hz  | 0.62 | 9.0 dB  |
| Peaking | 6950 Hz  | 2.81 | -6.7 dB |
| Peaking | 234 Hz   | 1.31 | -0.5 dB |
| Peaking | 747 Hz   | 1.51 | 1.1 dB  |
| Peaking | 1111 Hz  | 1.21 | -0.7 dB |
| Peaking | 1712 Hz  | 3.99 | 0.4 dB  |
| Peaking | 12157 Hz | 1.99 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VCO2/VSonic%20VCO2.png)