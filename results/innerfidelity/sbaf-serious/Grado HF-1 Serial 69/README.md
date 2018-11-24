# Grado HF-1 Serial 69

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.4; 41 4.2; 45 2.9; 49 1.8; 54 0.7; 60 -0.5; 66 -1.3; 72 -1.7; 79 -2.2; 87 -2.7; 96 -3.1; 106 -3.0; 116 -2.8; 128 -2.7; 141 -2.5; 155 -2.3; 170 -2.0; 187 -1.8; 206 -1.5; 227 -1.1; 249 -0.8; 274 -0.7; 302 -0.5; 332 -0.1; 365 -0.3; 402 -0.2; 442 0.1; 486 0.1; 535 0.1; 588 0.4; 647 0.5; 712 0.4; 783 0.5; 861 0.3; 947 -0.0; 1042 -0.2; 1146 -0.4; 1261 -1.0; 1387 -2.1; 1526 -3.3; 1678 -4.0; 1846 -4.7; 2031 -5.7; 2234 -5.6; 2457 -5.9; 2703 -5.5; 2973 -3.5; 3270 -1.6; 3597 -0.7; 3957 -2.7; 4353 -3.7; 4788 -3.0; 5267 -1.7; 5793 0.6; 6373 0.6; 7010 -3.7; 7711 -4.9; 8482 -8.3; 9330 -9.4; 10263 -1.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado HF-1 Serial 69 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Serial 69 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.73 | 7.3 dB   |
| Peaking | 89 Hz    | 0.74 | -4.4 dB  |
| Peaking | 1770 Hz  | 2.84 | -2.4 dB  |
| Peaking | 2427 Hz  | 1.82 | -5.4 dB  |
| Peaking | 8854 Hz  | 3.97 | -10.4 dB |
| Peaking | 3583 Hz  | 4.67 | 2.9 dB   |
| Peaking | 4354 Hz  | 2.96 | -3.7 dB  |
| Peaking | 6198 Hz  | 4.52 | 3.9 dB   |
| Peaking | 7053 Hz  | 4.96 | -2.8 dB  |
| Peaking | 10947 Hz | 5.89 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Serial%2069/Grado%20HF-1%20Serial%2069.png)