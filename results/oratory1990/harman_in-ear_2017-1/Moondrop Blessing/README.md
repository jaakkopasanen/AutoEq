# Moondrop Blessing

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.8; 60 5.3; 66 4.6; 72 4.2; 79 3.5; 87 3.0; 96 2.8; 106 1.9; 116 1.6; 128 0.9; 141 0.6; 155 0.0; 170 -0.5; 187 -1.1; 206 -1.4; 227 -1.8; 249 -1.9; 274 -1.9; 302 -1.7; 332 -1.5; 365 -1.3; 402 -1.1; 442 -1.0; 486 -0.8; 535 -0.7; 588 -0.5; 647 -0.3; 712 -0.0; 783 0.2; 861 0.4; 947 0.2; 1042 -0.2; 1146 -1.0; 1261 -1.6; 1387 -1.8; 1526 -1.6; 1678 -1.4; 1846 -1.1; 2031 -0.9; 2234 -0.7; 2457 -0.8; 2703 -0.8; 2973 -0.4; 3270 0.4; 3597 0.8; 3957 0.7; 4353 0.3; 4788 0.2; 5267 0.4; 5793 1.7; 6373 4.3; 7010 2.5; 7711 -0.3; 8482 -0.4; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -7.7; 15026 -19.5; 16529 -24.1; 18182 -22.4; 20000 -21.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Moondrop Blessing GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Moondrop Blessing ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.4  | 6.4 dB   |
| Peaking | 232 Hz   | 0.94 | -2.7 dB  |
| Peaking | 1501 Hz  | 2.52 | -1.7 dB  |
| Peaking | 10550 Hz | 0.34 | 23.6 dB  |
| Peaking | 16820 Hz | 0.37 | -40.6 dB |
| Peaking | 860 Hz   | 4.26 | 0.9 dB   |
| Peaking | 6527 Hz  | 4.72 | 4.8 dB   |
| Peaking | 8062 Hz  | 2.63 | -2.4 dB  |
| Peaking | 12625 Hz | 5    | 6.8 dB   |
| Peaking | 20782 Hz | 0.15 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Moondrop%20Blessing/Moondrop%20Blessing.png)