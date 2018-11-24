# T-Peos Rich 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 -4.1; 23 -4.0; 25 -4.0; 28 -4.1; 31 -4.1; 34 -4.1; 37 -4.2; 41 -4.3; 45 -4.3; 49 -4.5; 54 -4.6; 60 -4.8; 66 -5.0; 72 -5.2; 79 -5.5; 87 -5.7; 96 -6.0; 106 -6.0; 116 -6.0; 128 -6.1; 141 -6.1; 155 -6.0; 170 -5.8; 187 -5.6; 206 -5.4; 227 -4.9; 249 -4.6; 274 -4.1; 302 -3.6; 332 -3.2; 365 -2.6; 402 -2.1; 442 -1.5; 486 -1.1; 535 -0.6; 588 0.1; 647 0.4; 712 0.6; 783 0.9; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -2.2; 1526 -3.2; 1678 -4.1; 1846 -4.7; 2031 -5.0; 2234 -4.8; 2457 -3.0; 2703 -0.8; 2973 2.1; 3270 4.2; 3597 4.5; 3957 2.7; 4353 -1.7; 4788 -6.5; 5267 -7.8; 5793 -3.4; 6373 0.1; 7010 -0.1; 7711 -3.4; 8482 -6.0; 9330 -4.8; 10263 -1.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Rich 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Rich 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.27 | -4.1 dB  |
| Peaking | 167 Hz   | 0.75 | -4.2 dB  |
| Peaking | 1920 Hz  | 2.92 | -5.7 dB  |
| Peaking | 8622 Hz  | 3.18 | -6.1 dB  |
| Peaking | 24000 Hz | 2.29 | -3.8 dB  |
| Peaking | 742 Hz   | 2.71 | 1.7 dB   |
| Peaking | 2388 Hz  | 3.87 | -2.8 dB  |
| Peaking | 3553 Hz  | 2.38 | 7.3 dB   |
| Peaking | 5084 Hz  | 3.22 | -10.4 dB |
| Peaking | 6535 Hz  | 3.86 | 3.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Rich%20200/T-Peos%20Rich%20200.png)