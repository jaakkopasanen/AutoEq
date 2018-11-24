# Phiaton MS 400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.4; 41 4.9; 45 4.3; 49 3.6; 54 2.9; 60 2.3; 66 2.7; 72 2.9; 79 1.8; 87 0.9; 96 0.3; 106 -0.1; 116 -0.3; 128 -0.3; 141 1.0; 155 2.6; 170 2.0; 187 2.1; 206 2.2; 227 1.6; 249 1.5; 274 1.7; 302 1.9; 332 2.1; 365 2.5; 402 2.7; 442 2.7; 486 2.5; 535 2.6; 588 2.5; 647 2.5; 712 2.4; 783 2.3; 861 2.0; 947 0.5; 1042 -0.3; 1146 -0.4; 1261 -0.5; 1387 -1.0; 1526 -1.7; 1678 -2.1; 1846 -1.5; 2031 0.0; 2234 2.4; 2457 4.7; 2703 5.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.82 | 6.5 dB  |
| Peaking | 182 Hz  | 3.37 | 1.6 dB  |
| Peaking | 497 Hz  | 0.85 | 2.7 dB  |
| Peaking | 1676 Hz | 1.61 | -5.5 dB |
| Peaking | 3467 Hz | 0.77 | 7.5 dB  |
| Peaking | 115 Hz  | 4.67 | -1.5 dB |
| Peaking | 2651 Hz | 3.74 | 2.1 dB  |
| Peaking | 3213 Hz | 1.29 | -1.4 dB |
| Peaking | 6224 Hz | 2.1  | 5.8 dB  |
| Peaking | 7444 Hz | 1.5  | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20400/Phiaton%20MS%20400.png)