# Shure SRH440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.4; 31 4.7; 34 4.2; 37 3.7; 41 3.2; 45 2.7; 49 2.4; 54 2.0; 60 1.7; 66 1.3; 72 0.9; 79 0.2; 87 -0.5; 96 -1.0; 106 -1.1; 116 -0.7; 128 0.1; 141 0.4; 155 0.9; 170 1.5; 187 2.0; 206 2.1; 227 1.8; 249 1.4; 274 1.0; 302 0.5; 332 -0.0; 365 -0.7; 402 -0.7; 442 -0.4; 486 -0.2; 535 0.0; 588 0.1; 647 0.3; 712 0.3; 783 0.1; 861 0.0; 947 -0.0; 1042 0.2; 1146 -0.6; 1261 -1.1; 1387 -1.7; 1526 -2.3; 1678 -2.8; 1846 -3.0; 2031 -2.4; 2234 -1.1; 2457 0.5; 2703 1.1; 2973 1.8; 3270 1.7; 3597 2.1; 3957 1.5; 4353 0.7; 4788 1.2; 5267 2.4; 5793 4.1; 6373 4.1; 7010 2.4; 7711 -0.3; 8482 -3.5; 9330 -5.9; 10263 -3.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.06 | 6.2 dB   |
| Peaking | 206 Hz  | 3.14 | 2.3 dB   |
| Peaking | 1744 Hz | 2.56 | -3.6 dB  |
| Peaking | 7161 Hz | 0.89 | 5.6 dB   |
| Peaking | 9068 Hz | 2.51 | -10.4 dB |
| Peaking | 103 Hz  | 3.47 | -1.8 dB  |
| Peaking | 167 Hz  | 4.14 | 0.5 dB   |
| Peaking | 3467 Hz | 1.9  | 2.8 dB   |
| Peaking | 4660 Hz | 1.37 | -3.4 dB  |
| Peaking | 5882 Hz | 3.13 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Shure%20SRH440/Shure%20SRH440.png)