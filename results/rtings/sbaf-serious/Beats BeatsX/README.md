# Beats BeatsX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.9; 28 1.8; 31 1.7; 34 1.6; 37 1.5; 41 1.4; 45 1.3; 49 1.3; 54 1.2; 60 0.9; 66 0.7; 72 0.7; 79 0.8; 87 1.0; 96 1.2; 106 1.1; 116 1.0; 128 1.0; 141 1.0; 155 1.1; 170 1.3; 187 1.5; 206 1.6; 227 1.9; 249 2.1; 274 2.2; 302 2.5; 332 2.8; 365 3.0; 402 3.2; 442 3.3; 486 3.5; 535 3.6; 588 3.6; 647 3.5; 712 3.2; 783 2.4; 861 1.4; 947 0.5; 1042 -0.2; 1146 -0.7; 1261 -0.8; 1387 -1.1; 1526 -1.4; 1678 -1.4; 1846 -1.2; 2031 -1.0; 2234 -0.6; 2457 0.1; 2703 1.8; 2973 4.6; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.6; 5793 5.7; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -1.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats BeatsX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats BeatsX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.2  | 2.0 dB  |
| Peaking | 381 Hz  | 0.69 | 2.6 dB  |
| Peaking | 648 Hz  | 1.69 | 2.5 dB  |
| Peaking | 1874 Hz | 0.82 | -3.8 dB |
| Peaking | 3963 Hz | 1.05 | 8.1 dB  |
| Peaking | 2594 Hz | 4.81 | -1.3 dB |
| Peaking | 3085 Hz | 3.95 | 2.1 dB  |
| Peaking | 3961 Hz | 3.96 | -1.2 dB |
| Peaking | 6244 Hz | 3.56 | 3.8 dB  |
| Peaking | 8370 Hz | 1.3  | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20BeatsX/Beats%20BeatsX.png)