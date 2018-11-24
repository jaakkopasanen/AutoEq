# Beyerdynamic DT 990 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.3; 28 2.6; 31 2.0; 34 1.5; 37 1.0; 41 0.4; 45 -0.0; 49 -0.4; 54 -0.9; 60 -1.3; 66 -1.7; 72 -2.0; 79 -2.3; 87 -2.1; 96 -2.2; 106 -2.9; 116 -3.3; 128 -3.5; 141 -3.6; 155 -3.5; 170 -3.3; 187 -3.2; 206 -3.0; 227 -2.5; 249 -2.0; 274 -1.4; 302 -0.8; 332 -0.2; 365 0.5; 402 0.8; 442 0.2; 486 0.7; 535 1.2; 588 1.6; 647 1.8; 712 2.0; 783 1.8; 861 1.3; 947 0.4; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -0.8; 1526 -0.3; 1678 -0.2; 1846 -0.0; 2031 -0.1; 2234 -0.4; 2457 -1.2; 2703 -2.1; 2973 -2.5; 3270 -1.8; 3597 -1.2; 3957 -2.0; 4353 -2.2; 4788 -3.1; 5267 -4.9; 5793 -7.7; 6373 -5.7; 7010 -2.6; 7711 -5.4; 8482 -6.9; 9330 -4.4; 10263 -4.3; 11289 -8.8; 12418 -13.0; 13660 -11.6; 15026 -8.8; 16529 -11.3; 18182 -14.9; 20000 -15.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.66 | 4.6 dB   |
| Peaking | 135 Hz   | 0.97 | -3.9 dB  |
| Peaking | 5789 Hz  | 2.39 | -5.3 dB  |
| Peaking | 12547 Hz | 3.59 | -7.6 dB  |
| Peaking | 19650 Hz | 0.49 | -16.2 dB |
| Peaking | 63 Hz    | 4.15 | -0.7 dB  |
| Peaking | 379 Hz   | 3.93 | 1.5 dB   |
| Peaking | 684 Hz   | 1.42 | 3.6 dB   |
| Peaking | 740 Hz   | 0.41 | -1.3 dB  |
| Peaking | 18057 Hz | 3.45 | -0.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20990%20250%20Ohm/Beyerdynamic%20DT%20990%20250%20Ohm.png)