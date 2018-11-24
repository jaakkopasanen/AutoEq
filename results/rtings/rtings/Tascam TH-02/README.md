# Tascam TH-02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.1; 28 4.6; 31 4.2; 34 3.8; 37 3.6; 41 3.5; 45 3.5; 49 3.4; 54 3.3; 60 3.1; 66 2.7; 72 2.4; 79 2.1; 87 1.8; 96 1.4; 106 1.0; 116 0.5; 128 -0.1; 141 -0.6; 155 -0.9; 170 -1.1; 187 -1.2; 206 -1.1; 227 -1.1; 249 -1.2; 274 -1.3; 302 -1.3; 332 -1.3; 365 -0.9; 402 -0.1; 442 0.0; 486 -0.6; 535 -1.3; 588 -1.8; 647 -2.1; 712 -2.2; 783 -2.2; 861 -1.7; 947 -0.3; 1042 0.0; 1146 0.1; 1261 -0.4; 1387 -0.7; 1526 -1.1; 1678 -1.0; 1846 0.5; 2031 2.6; 2234 4.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.6; 9330 -3.5; 10263 -2.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tascam TH-02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tascam TH-02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.84 | 5.7 dB  |
| Peaking | 58 Hz   | 1.49 | 2.3 dB  |
| Peaking | 1271 Hz | 0.36 | -3.5 dB |
| Peaking | 3745 Hz | 0.53 | 8.7 dB  |
| Peaking | 9287 Hz | 2.4  | -6.6 dB |
| Peaking | 188 Hz  | 1.8  | -1.0 dB |
| Peaking | 442 Hz  | 3.76 | 1.9 dB  |
| Peaking | 1119 Hz | 1.86 | 4.7 dB  |
| Peaking | 1423 Hz | 0.8  | -4.2 dB |
| Peaking | 2371 Hz | 2.84 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Tascam%20TH-02/Tascam%20TH-02.png)