# Etymotic Research ER4SR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 5.4; 155 4.5; 170 3.7; 187 3.0; 206 2.3; 227 1.9; 249 1.5; 274 1.3; 302 1.3; 332 1.4; 365 1.3; 402 1.3; 442 1.3; 486 1.3; 535 1.2; 588 1.1; 647 1.1; 712 1.1; 783 1.2; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.5; 1387 -2.0; 1526 -2.2; 1678 -2.3; 1846 -2.2; 2031 -2.0; 2234 -1.6; 2457 -1.3; 2703 -0.6; 2973 0.4; 3270 1.2; 3597 1.6; 3957 1.7; 4353 2.0; 4788 2.7; 5267 4.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -5.8; 15026 -17.5; 16529 -14.5; 18182 -1.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.28 | 6.6 dB   |
| Peaking | 772 Hz   | 1.89 | 1.3 dB   |
| Peaking | 1646 Hz  | 1.34 | -2.8 dB  |
| Peaking | 5802 Hz  | 1.96 | 6.2 dB   |
| Peaking | 15612 Hz | 3.21 | -20.8 dB |
| Peaking | 128 Hz   | 4.82 | 1.4 dB   |
| Peaking | 7739 Hz  | 5.86 | -1.7 dB  |
| Peaking | 12879 Hz | 2.82 | 5.2 dB   |
| Peaking | 14306 Hz | 4.99 | -6.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20Research%20ER4SR/Etymotic%20Research%20ER4SR.png)