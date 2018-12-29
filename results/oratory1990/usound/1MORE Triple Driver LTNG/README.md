# 1MORE Triple Driver LTNG

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 -0.7; 23 -1.1; 25 -1.4; 28 -1.8; 31 -2.2; 34 -2.4; 37 -2.7; 41 -3.0; 45 -3.2; 49 -3.4; 54 -3.7; 60 -4.0; 66 -4.2; 72 -4.5; 79 -4.8; 87 -5.1; 96 -5.4; 106 -5.6; 116 -5.8; 128 -5.9; 141 -6.0; 155 -5.9; 170 -5.8; 187 -5.6; 206 -5.3; 227 -5.0; 249 -4.7; 274 -4.3; 302 -3.9; 332 -3.5; 365 -3.0; 402 -2.7; 442 -2.3; 486 -1.8; 535 -1.4; 588 -1.0; 647 -0.6; 712 -0.2; 783 0.1; 861 0.2; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.0; 1387 -1.4; 1526 -1.7; 1678 -1.9; 1846 -2.2; 2031 -2.7; 2234 -3.6; 2457 -4.2; 2703 -4.0; 2973 -3.4; 3270 -3.0; 3597 -3.4; 3957 -5.0; 4353 -6.1; 4788 -3.2; 5267 2.8; 5793 5.3; 6373 3.1; 7010 0.0; 7711 -2.8; 8482 -1.3; 9330 0.0; 10263 0.0; 11289 -2.0; 12418 -5.1; 13660 -7.6; 15026 -9.9; 16529 -11.7; 18182 -4.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver LTNG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver LTNG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 128 Hz   | 0.43 | -6.0 dB  |
| Peaking | 2448 Hz  | 1.85 | -3.7 dB  |
| Peaking | 4393 Hz  | 2.98 | -6.9 dB  |
| Peaking | 5650 Hz  | 3.99 | 8.5 dB   |
| Peaking | 15900 Hz | 1.52 | -12.3 dB |
| Peaking | 37 Hz    | 2.14 | -0.5 dB  |
| Peaking | 816 Hz   | 2.96 | 1.3 dB   |
| Peaking | 7796 Hz  | 5.63 | -3.8 dB  |
| Peaking | 10795 Hz | 1.27 | 3.3 dB   |
| Peaking | 12697 Hz | 2.54 | -3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/1MORE%20Triple%20Driver%20LTNG/1MORE%20Triple%20Driver%20LTNG.png)