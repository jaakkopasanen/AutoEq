# Bowers & Wilkins P5 Series 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -3.1; 23 -3.4; 25 -3.7; 28 -4.1; 31 -4.4; 34 -4.5; 37 -4.5; 41 -4.5; 45 -4.5; 49 -4.5; 54 -4.6; 60 -4.6; 66 -4.7; 72 -4.8; 79 -4.8; 87 -4.8; 96 -4.7; 106 -4.6; 116 -4.4; 128 -4.1; 141 -3.6; 155 -3.2; 170 -2.7; 187 -2.3; 206 -1.7; 227 -1.0; 249 -0.3; 274 0.5; 302 1.5; 332 2.6; 365 3.7; 402 3.9; 442 3.3; 486 2.5; 535 2.0; 588 1.7; 647 1.4; 712 1.2; 783 1.0; 861 0.7; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.9; 1526 -4.1; 1678 -5.2; 1846 -6.3; 2031 -6.7; 2234 -6.5; 2457 -5.7; 2703 -4.1; 2973 -1.1; 3270 0.6; 3597 0.4; 3957 0.0; 4353 0.3; 4788 2.3; 5267 3.7; 5793 2.2; 6373 -0.4; 7010 1.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Series 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.82 | -2.5 dB |
| Peaking | 101 Hz  | 0.39 | -4.7 dB |
| Peaking | 389 Hz  | 1.03 | 5.2 dB  |
| Peaking | 2003 Hz | 1.79 | -7.5 dB |
| Peaking | 5147 Hz | 3.45 | 4.1 dB  |
| Peaking | 519 Hz  | 4.88 | -0.7 dB |
| Peaking | 1498 Hz | 1.88 | -3.4 dB |
| Peaking | 1846 Hz | 0.95 | 4.4 dB  |
| Peaking | 2797 Hz | 1.44 | -5.5 dB |
| Peaking | 3159 Hz | 3.29 | 5.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)