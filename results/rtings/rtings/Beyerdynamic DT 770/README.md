# Beyerdynamic DT 770

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 -1.1; 23 -1.4; 25 -1.7; 28 -2.1; 31 -2.3; 34 -2.4; 37 -2.4; 41 -2.2; 45 -1.9; 49 -1.5; 54 -1.1; 60 -0.7; 66 -0.6; 72 -0.6; 79 -0.7; 87 -0.9; 96 -1.1; 106 -1.2; 116 -1.2; 128 -0.9; 141 -0.4; 155 0.6; 170 1.7; 187 2.7; 206 3.1; 227 2.7; 249 2.1; 274 1.3; 302 0.7; 332 0.3; 365 0.1; 402 -0.4; 442 -0.7; 486 -0.8; 535 -0.8; 588 -0.7; 647 -0.6; 712 -0.4; 783 -0.5; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.1; 1261 -0.4; 1387 -0.9; 1526 -1.2; 1678 -1.6; 1846 -2.1; 2031 -2.8; 2234 -2.9; 2457 -2.1; 2703 -0.6; 2973 1.5; 3270 4.7; 3597 5.7; 3957 0.4; 4353 -2.6; 4788 -0.0; 5267 2.7; 5793 1.3; 6373 -4.2; 7010 -3.2; 7711 -3.9; 8482 -8.3; 9330 -10.0; 10263 -4.7; 11289 -0.1; 12418 -0.8; 13660 -4.4; 15026 -4.1; 16529 -3.1; 18182 -5.3; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 212 Hz   | 3.35 | 3.5 dB   |
| Peaking | 2130 Hz  | 1.98 | -3.1 dB  |
| Peaking | 3405 Hz  | 5.52 | 7.4 dB   |
| Peaking | 8998 Hz  | 3.83 | -10.2 dB |
| Peaking | 20000 Hz | 0.59 | -6.7 dB  |
| Peaking | 32 Hz    | 0.45 | -1.9 dB  |
| Peaking | 4402 Hz  | 7.32 | -4.2 dB  |
| Peaking | 5527 Hz  | 3.53 | 5.0 dB   |
| Peaking | 6405 Hz  | 5.41 | -5.0 dB  |
| Peaking | 11507 Hz | 7.59 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beyerdynamic%20DT%20770/Beyerdynamic%20DT%20770.png)