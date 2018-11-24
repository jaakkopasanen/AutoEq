# Phiaton MS 100 BA

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.9; 28 0.7; 31 0.5; 34 0.3; 37 0.2; 41 -0.1; 45 -0.3; 49 -0.5; 54 -0.7; 60 -1.1; 66 -1.5; 72 -1.8; 79 -2.2; 87 -2.6; 96 -3.1; 106 -3.4; 116 -3.6; 128 -3.9; 141 -4.1; 155 -4.3; 170 -4.4; 187 -4.4; 206 -4.5; 227 -4.4; 249 -4.3; 274 -4.1; 302 -3.9; 332 -3.6; 365 -3.3; 402 -2.9; 442 -2.4; 486 -2.1; 535 -1.6; 588 -0.9; 647 -0.5; 712 -0.2; 783 0.2; 861 0.2; 947 0.2; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -0.9; 1526 -1.3; 1678 -1.7; 1846 -1.5; 2031 -1.1; 2234 -0.2; 2457 1.9; 2703 3.5; 2973 4.7; 3270 5.2; 3597 5.6; 3957 5.9; 4353 5.3; 4788 5.7; 5267 6.0; 5793 5.1; 6373 1.0; 7010 1.9; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 100 BA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 100 BA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.69 | 1.4 dB  |
| Peaking | 150 Hz  | 0.67 | -4.0 dB |
| Peaking | 315 Hz  | 1.27 | -2.1 dB |
| Peaking | 1855 Hz | 2.28 | -3.3 dB |
| Peaking | 3903 Hz | 1.11 | 6.6 dB  |
| Peaking | 820 Hz  | 3.13 | 0.8 dB  |
| Peaking | 2892 Hz | 3.43 | 1.4 dB  |
| Peaking | 5482 Hz | 3.89 | 4.6 dB  |
| Peaking | 5507 Hz | 0.57 | -1.3 dB |
| Peaking | 6224 Hz | 2.43 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20100%20BA/Phiaton%20MS%20100%20BA.png)