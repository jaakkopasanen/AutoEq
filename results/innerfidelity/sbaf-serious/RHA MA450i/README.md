# RHA MA450i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -11.8; 23 -11.7; 25 -11.7; 28 -11.6; 31 -11.4; 34 -11.3; 37 -11.2; 41 -11.0; 45 -10.9; 49 -10.8; 54 -10.7; 60 -10.6; 66 -10.5; 72 -10.4; 79 -10.3; 87 -10.3; 96 -10.2; 106 -10.0; 116 -9.7; 128 -9.4; 141 -9.2; 155 -8.8; 170 -8.3; 187 -8.0; 206 -7.4; 227 -6.8; 249 -6.3; 274 -5.6; 302 -5.1; 332 -4.3; 365 -3.8; 402 -3.1; 442 -2.4; 486 -2.1; 535 -1.5; 588 -0.9; 647 -0.4; 712 -0.2; 783 0.0; 861 0.3; 947 0.0; 1042 -0.0; 1146 -0.3; 1261 -0.5; 1387 -1.1; 1526 -1.7; 1678 -1.8; 1846 -1.8; 2031 -1.5; 2234 -1.3; 2457 -1.0; 2703 -1.1; 2973 -1.1; 3270 -1.3; 3597 -1.6; 3957 -2.8; 4353 -6.0; 4788 -9.9; 5267 -11.4; 5793 -4.0; 6373 1.1; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.1; 16529 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA MA450i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA450i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.17 | -11.4 dB |
| Peaking | 170 Hz   | 0.66 | -4.4 dB  |
| Peaking | 1769 Hz  | 3.15 | -1.7 dB  |
| Peaking | 5103 Hz  | 3.39 | -13.3 dB |
| Peaking | 6609 Hz  | 3.78 | 5.8 dB   |
| Peaking | 166 Hz   | 2.48 | 0.5 dB   |
| Peaking | 325 Hz   | 1.68 | -0.5 dB  |
| Peaking | 771 Hz   | 1.93 | 1.2 dB   |
| Peaking | 13578 Hz | 2.07 | 0.5 dB   |
| Peaking | 15196 Hz | 5.29 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20MA450i/RHA%20MA450i.png)