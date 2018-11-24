# Koss Porta Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.0; 31 3.8; 34 2.8; 37 1.9; 41 0.8; 45 -0.1; 49 -0.9; 54 -1.7; 60 -2.4; 66 -3.0; 72 -3.4; 79 -3.8; 87 -4.2; 96 -4.5; 106 -4.9; 116 -5.1; 128 -5.3; 141 -5.3; 155 -5.3; 170 -5.0; 187 -4.8; 206 -4.5; 227 -4.0; 249 -3.6; 274 -3.2; 302 -2.9; 332 -2.5; 365 -2.1; 402 -1.8; 442 -1.5; 486 -1.1; 535 -0.8; 588 -0.5; 647 -0.2; 712 0.0; 783 0.1; 861 0.1; 947 0.1; 1042 0.0; 1146 -0.1; 1261 -0.5; 1387 -1.5; 1526 -2.5; 1678 -3.1; 1846 -3.4; 2031 -3.6; 2234 -3.1; 2457 -1.9; 2703 -0.2; 2973 0.6; 3270 1.2; 3597 2.4; 3957 5.8; 4353 6.0; 4788 3.0; 5267 -0.8; 5793 4.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.2  | 6.9 dB  |
| Peaking | 130 Hz  | 0.54 | -5.6 dB |
| Peaking | 1945 Hz | 2.39 | -4.1 dB |
| Peaking | 4124 Hz | 4.17 | 6.8 dB  |
| Peaking | 6317 Hz | 6.44 | 6.0 dB  |
| Peaking | 866 Hz  | 1.43 | 0.9 dB  |
| Peaking | 1526 Hz | 6.15 | -1.1 dB |
| Peaking | 5234 Hz | 8.43 | -6.0 dB |
| Peaking | 5259 Hz | 3.03 | 2.9 dB  |
| Peaking | 8031 Hz | 2.19 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)