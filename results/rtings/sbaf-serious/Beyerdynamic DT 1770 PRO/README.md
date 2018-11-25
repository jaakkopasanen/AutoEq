# Beyerdynamic DT 1770 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.3; 28 0.9; 31 0.5; 34 0.3; 37 0.1; 41 -0.0; 45 -0.1; 49 -0.1; 54 -0.2; 60 -0.3; 66 -0.4; 72 -0.4; 79 -0.5; 87 -0.7; 96 -1.0; 106 -1.3; 116 -1.5; 128 -1.5; 141 -1.1; 155 -0.4; 170 0.6; 187 2.0; 206 3.5; 227 4.5; 249 4.2; 274 2.8; 302 1.2; 332 0.1; 365 -0.4; 402 -0.4; 442 -0.2; 486 -0.2; 535 -0.3; 588 -0.3; 647 -0.2; 712 -0.2; 783 -0.3; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.5; 1387 0.1; 1526 -0.5; 1678 -0.5; 1846 0.4; 2031 1.4; 2234 0.7; 2457 1.6; 2703 2.7; 2973 4.4; 3270 5.8; 3597 6.0; 3957 6.0; 4353 4.4; 4788 0.3; 5267 1.7; 5793 1.9; 6373 -0.8; 7010 0.7; 7711 -0.7; 8482 -3.1; 9330 -2.4; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 1.08 | 2.8 dB  |
| Peaking | 199 Hz   | 0.66 | -3.9 dB |
| Peaking | 228 Hz   | 1.78 | 8.5 dB  |
| Peaking | 3559 Hz  | 2.21 | 6.7 dB  |
| Peaking | 8714 Hz  | 5.31 | -4.0 dB |
| Peaking | 354 Hz   | 7.09 | -0.5 dB |
| Peaking | 1502 Hz  | 1.83 | 1.0 dB  |
| Peaking | 1604 Hz  | 4.24 | -2.0 dB |
| Peaking | 10551 Hz | 4.39 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beyerdynamic%20DT%201770%20PRO/Beyerdynamic%20DT%201770%20PRO.png)