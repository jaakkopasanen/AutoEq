# Koss Porta Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 4.9; 31 3.8; 34 2.8; 37 2.0; 41 1.0; 45 0.2; 49 -0.6; 54 -1.3; 60 -2.1; 66 -2.8; 72 -3.4; 79 -4.0; 87 -4.5; 96 -5.0; 106 -5.3; 116 -5.6; 128 -5.8; 141 -5.9; 155 -5.9; 170 -5.7; 187 -5.4; 206 -5.0; 227 -4.5; 249 -4.2; 274 -3.9; 302 -3.7; 332 -3.4; 365 -3.1; 402 -2.8; 442 -2.6; 486 -2.3; 535 -2.0; 588 -1.6; 647 -1.2; 712 -0.8; 783 -0.4; 861 -0.0; 947 0.0; 1042 -0.0; 1146 -0.3; 1261 -0.8; 1387 -1.4; 1526 -2.1; 1678 -2.7; 1846 -3.5; 2031 -4.0; 2234 -3.6; 2457 -2.4; 2703 -0.8; 2973 -0.4; 3270 -0.6; 3597 0.3; 3957 5.2; 4353 6.0; 4788 3.2; 5267 -1.3; 5793 2.9; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.3; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.85 | 6.9 dB  |
| Peaking | 134 Hz  | 0.45 | -6.1 dB |
| Peaking | 2032 Hz | 2.28 | -4.1 dB |
| Peaking | 4253 Hz | 5.79 | 7.2 dB  |
| Peaking | 6381 Hz | 6.85 | 5.8 dB  |
| Peaking | 466 Hz  | 2.31 | -0.5 dB |
| Peaking | 915 Hz  | 2.95 | 1.1 dB  |
| Peaking | 5146 Hz | 3.5  | 2.2 dB  |
| Peaking | 5202 Hz | 9.05 | -5.3 dB |
| Peaking | 9550 Hz | 8.07 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)