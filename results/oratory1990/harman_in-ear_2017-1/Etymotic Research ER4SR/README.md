# Etymotic Research ER4SR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.9; 79 5.5; 87 5.0; 96 4.5; 106 4.0; 116 3.6; 128 3.2; 141 2.8; 155 2.4; 170 2.2; 187 2.0; 206 1.7; 227 1.6; 249 1.4; 274 1.3; 302 1.3; 332 1.4; 365 1.3; 402 1.3; 442 1.3; 486 1.3; 535 1.2; 588 1.1; 647 1.1; 712 1.1; 783 1.2; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.5; 1387 -2.0; 1526 -2.2; 1678 -2.3; 1846 -2.2; 2031 -2.0; 2234 -1.6; 2457 -1.3; 2703 -0.6; 2973 0.4; 3270 1.2; 3597 1.6; 3957 1.7; 4353 2.0; 4788 2.7; 5267 4.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -5.8; 15026 -17.5; 16529 -14.5; 18182 -1.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.34 | 6.4 dB   |
| Peaking | 758 Hz   | 0.71 | 1.5 dB   |
| Peaking | 1588 Hz  | 1.24 | -3.3 dB  |
| Peaking | 5803 Hz  | 1.96 | 6.2 dB   |
| Peaking | 15612 Hz | 3.21 | -20.8 dB |
| Peaking | 2445 Hz  | 3.4  | -0.6 dB  |
| Peaking | 3333 Hz  | 4.08 | 1.1 dB   |
| Peaking | 7822 Hz  | 5.54 | -1.7 dB  |
| Peaking | 13010 Hz | 2.85 | 5.2 dB   |
| Peaking | 14468 Hz | 5.02 | -6.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20Research%20ER4SR/Etymotic%20Research%20ER4SR.png)