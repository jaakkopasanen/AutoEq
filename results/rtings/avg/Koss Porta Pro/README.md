# Koss Porta Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 4.9; 31 3.8; 34 2.8; 37 2.0; 41 1.0; 45 0.2; 49 -0.6; 54 -1.3; 60 -2.1; 66 -2.8; 72 -3.4; 79 -4.0; 87 -4.5; 96 -5.0; 106 -5.3; 116 -5.6; 128 -5.8; 141 -5.9; 155 -5.9; 170 -5.7; 187 -5.4; 206 -5.0; 227 -4.5; 249 -4.2; 274 -3.9; 302 -3.7; 332 -3.4; 365 -3.1; 402 -2.8; 442 -2.6; 486 -2.3; 535 -2.0; 588 -1.6; 647 -1.2; 712 -0.8; 783 -0.4; 861 -0.0; 947 0.0; 1042 -0.0; 1146 -0.3; 1261 -0.8; 1387 -1.4; 1526 -2.1; 1678 -2.7; 1846 -3.5; 2031 -4.0; 2234 -3.6; 2457 -2.4; 2703 -1.1; 2973 -0.9; 3270 -1.4; 3597 -0.7; 3957 4.1; 4353 6.0; 4788 1.4; 5267 -3.8; 5793 0.5; 6373 4.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.86 | 6.9 dB  |
| Peaking | 135 Hz  | 0.46 | -6.1 dB |
| Peaking | 2163 Hz | 1.96 | -4.9 dB |
| Peaking | 2467 Hz | 3.41 | 1.7 dB  |
| Peaking | 4253 Hz | 7.22 | 7.5 dB  |
| Peaking | 945 Hz  | 3.25 | 1.1 dB  |
| Peaking | 4618 Hz | 8.74 | 3.3 dB  |
| Peaking | 5250 Hz | 5.64 | -5.3 dB |
| Peaking | 6035 Hz | 1.14 | -1.1 dB |
| Peaking | 6409 Hz | 4.21 | 6.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)