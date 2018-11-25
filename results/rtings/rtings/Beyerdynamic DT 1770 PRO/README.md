# Beyerdynamic DT 1770 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.3; 25 1.0; 28 0.7; 31 0.5; 34 0.3; 37 0.2; 41 0.2; 45 0.2; 49 0.2; 54 0.1; 60 0.0; 66 -0.2; 72 -0.4; 79 -0.7; 87 -1.0; 96 -1.4; 106 -1.8; 116 -2.0; 128 -2.0; 141 -1.7; 155 -1.1; 170 -0.0; 187 1.4; 206 3.0; 227 4.0; 249 3.7; 274 2.1; 302 0.4; 332 -0.8; 365 -1.4; 402 -1.5; 442 -1.3; 486 -1.4; 535 -1.4; 588 -1.4; 647 -1.2; 712 -1.1; 783 -0.8; 861 -0.4; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.3; 1387 0.1; 1526 -0.1; 1678 -0.2; 1846 0.4; 2031 1.0; 2234 0.2; 2457 1.2; 2703 2.1; 2973 3.4; 3270 3.9; 3597 4.2; 3957 5.8; 4353 4.4; 4788 0.4; 5267 1.3; 5793 0.5; 6373 -3.4; 7010 -1.8; 7711 -1.9; 8482 -3.5; 9330 -3.9; 10263 -1.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.16 | 1.2 dB  |
| Peaking | 208 Hz   | 0.53 | -5.1 dB |
| Peaking | 229 Hz   | 1.77 | 9.2 dB  |
| Peaking | 3775 Hz  | 1.92 | 5.8 dB  |
| Peaking | 7970 Hz  | 1.46 | -3.7 dB |
| Peaking | 1116 Hz  | 3.75 | 0.6 dB  |
| Peaking | 7807 Hz  | 4.94 | 3.4 dB  |
| Peaking | 8919 Hz  | 1.56 | -3.3 dB |
| Peaking | 10822 Hz | 4.65 | 1.8 dB  |
| Peaking | 11347 Hz | 1.06 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beyerdynamic%20DT%201770%20PRO/Beyerdynamic%20DT%201770%20PRO.png)