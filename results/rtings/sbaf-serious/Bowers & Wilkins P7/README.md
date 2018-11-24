# Bowers & Wilkins P7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.8; 23 -2.1; 25 -2.4; 28 -2.8; 31 -3.1; 34 -3.2; 37 -3.2; 41 -3.2; 45 -3.1; 49 -3.0; 54 -2.9; 60 -2.8; 66 -2.8; 72 -2.5; 79 -2.1; 87 -2.0; 96 -2.3; 106 -2.6; 116 -2.8; 128 -2.8; 141 -2.7; 155 -2.3; 170 -1.9; 187 -1.4; 206 -0.7; 227 0.2; 249 1.1; 274 2.0; 302 2.5; 332 2.8; 365 2.6; 402 1.8; 442 1.6; 486 1.7; 535 1.7; 588 1.5; 647 1.4; 712 1.2; 783 0.7; 861 0.2; 947 0.0; 1042 0.3; 1146 0.7; 1261 0.0; 1387 -0.8; 1526 -2.0; 1678 -2.9; 1846 -3.1; 2031 -2.3; 2234 0.8; 2457 3.8; 2703 4.7; 2973 5.4; 3270 5.4; 3597 4.1; 3957 2.6; 4353 2.9; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -0.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.73 | -3.4 dB  |
| Peaking | 128 Hz  | 2.38 | -2.6 dB  |
| Peaking | 1828 Hz | 1.48 | -14.6 dB |
| Peaking | 2175 Hz | 0.73 | 11.7 dB  |
| Peaking | 5734 Hz | 4.06 | 4.5 dB   |
| Peaking | 335 Hz  | 2.15 | 2.8 dB   |
| Peaking | 934 Hz  | 4.72 | -1.2 dB  |
| Peaking | 4092 Hz | 4.23 | -4.1 dB  |
| Peaking | 4103 Hz | 1.68 | 2.4 dB   |
| Peaking | 8657 Hz | 3.22 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)