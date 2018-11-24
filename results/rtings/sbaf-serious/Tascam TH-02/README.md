# Tascam TH-02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.4; 28 4.8; 31 4.2; 34 3.8; 37 3.5; 41 3.3; 45 3.2; 49 3.1; 54 3.0; 60 2.8; 66 2.5; 72 2.4; 79 2.3; 87 2.1; 96 1.9; 106 1.5; 116 1.0; 128 0.4; 141 -0.0; 155 -0.3; 170 -0.4; 187 -0.6; 206 -0.6; 227 -0.6; 249 -0.6; 274 -0.6; 302 -0.5; 332 -0.4; 365 0.1; 402 0.9; 442 1.1; 486 0.6; 535 -0.1; 588 -0.7; 647 -1.0; 712 -1.3; 783 -1.8; 861 -1.5; 947 -0.3; 1042 0.1; 1146 0.3; 1261 -0.1; 1387 -0.7; 1526 -1.4; 1678 -1.4; 1846 0.6; 2031 3.0; 2234 5.2; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.2; 9330 -2.0; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tascam TH-02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tascam TH-02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.73 | 5.7 dB  |
| Peaking | 71 Hz   | 1.61 | 1.7 dB  |
| Peaking | 1570 Hz | 0.65 | -8.2 dB |
| Peaking | 2833 Hz | 0.47 | 11.0 dB |
| Peaking | 8955 Hz | 2.5  | -5.1 dB |
| Peaking | 446 Hz  | 1.98 | 3.0 dB  |
| Peaking | 1128 Hz | 2.28 | 3.9 dB  |
| Peaking | 1202 Hz | 0.24 | -2.5 dB |
| Peaking | 2329 Hz | 3.03 | 3.5 dB  |
| Peaking | 5817 Hz | 2.73 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Tascam%20TH-02/Tascam%20TH-02.png)