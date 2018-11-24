# FLC Technology FLC8 C C Gn Strin

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.8; 49 5.5; 54 5.2; 60 4.8; 66 4.4; 72 4.1; 79 3.6; 87 3.1; 96 2.5; 106 2.2; 116 1.9; 128 1.5; 141 1.1; 155 1.0; 170 0.8; 187 0.6; 206 0.5; 227 0.5; 249 0.4; 274 0.6; 302 0.6; 332 0.7; 365 0.9; 402 1.0; 442 1.3; 486 1.3; 535 1.5; 588 1.9; 647 1.9; 712 1.6; 783 1.7; 861 1.4; 947 0.6; 1042 -0.4; 1146 -1.2; 1261 -1.5; 1387 -1.5; 1526 -0.7; 1678 0.3; 1846 1.6; 2031 2.3; 2234 2.3; 2457 2.0; 2703 1.3; 2973 4.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 3.6; 4788 4.4; 5267 6.0; 5793 5.7; 6373 0.7; 7010 -6.6; 7711 -6.8; 8482 -4.4; 9330 -4.6; 10263 -6.1; 11289 -3.8; 12418 -0.1; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technology FLC8 C C Gn Strin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Gn Strin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.43 | 6.3 dB   |
| Peaking | 3524 Hz  | 2.19 | 6.0 dB   |
| Peaking | 5743 Hz  | 2.72 | 8.6 dB   |
| Peaking | 7239 Hz  | 2.86 | -10.4 dB |
| Peaking | 10303 Hz | 4.08 | -5.7 dB  |
| Peaking | 739 Hz   | 1.13 | 2.5 dB   |
| Peaking | 1325 Hz  | 1.45 | -3.5 dB  |
| Peaking | 1981 Hz  | 1.88 | 2.5 dB   |
| Peaking | 2751 Hz  | 8.85 | -2.3 dB  |
| Peaking | 12803 Hz | 6.16 | 1.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin.png)