# Bowers & Wilkins P5 S2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 -2.7; 23 -3.1; 25 -3.5; 28 -4.0; 31 -4.3; 34 -4.5; 37 -4.7; 41 -4.7; 45 -4.8; 49 -4.9; 54 -4.9; 60 -4.9; 66 -4.9; 72 -4.8; 79 -4.6; 87 -4.4; 96 -4.3; 106 -4.1; 116 -3.9; 128 -3.6; 141 -3.1; 155 -2.6; 170 -2.1; 187 -1.7; 206 -1.2; 227 -0.6; 249 0.2; 274 1.2; 302 2.3; 332 3.6; 365 4.7; 402 5.0; 442 4.4; 486 3.7; 535 3.2; 588 2.8; 647 2.5; 712 2.1; 783 1.5; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.6; 1387 -2.9; 1526 -4.4; 1678 -5.6; 1846 -6.3; 2031 -6.3; 2234 -6.0; 2457 -5.2; 2703 -3.6; 2973 -0.0; 3270 2.5; 3597 2.5; 3957 1.2; 4353 0.3; 4788 2.2; 5267 4.1; 5793 3.7; 6373 2.2; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 S2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 0.64 | -2.4 dB  |
| Peaking | 122 Hz  | 0.3  | -4.4 dB  |
| Peaking | 401 Hz  | 0.82 | 7.2 dB   |
| Peaking | 2108 Hz | 1.22 | -10.4 dB |
| Peaking | 3496 Hz | 0.75 | 5.5 dB   |
| Peaking | 2665 Hz | 6.87 | -2.1 dB  |
| Peaking | 3335 Hz | 2.72 | 2.2 dB   |
| Peaking | 4345 Hz | 3.25 | -4.8 dB  |
| Peaking | 5259 Hz | 2.17 | 3.4 dB   |
| Peaking | 8653 Hz | 1.66 | -1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bowers%20&%20Wilkins%20P5%20S2/Bowers%20&%20Wilkins%20P5%20S2.png)