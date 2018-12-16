# Etymotic Research ER4SR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.9; 87 5.4; 96 4.9; 106 4.4; 116 3.9; 128 3.5; 141 3.1; 155 2.8; 170 2.5; 187 2.3; 206 2.1; 227 2.0; 249 1.8; 274 1.6; 302 1.6; 332 1.5; 365 1.4; 402 1.4; 442 1.3; 486 1.2; 535 1.1; 588 0.9; 647 0.9; 712 1.0; 783 1.0; 861 0.8; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.7; 1526 -3.1; 1678 -3.2; 1846 -3.2; 2031 -3.4; 2234 -3.6; 2457 -3.8; 2703 -3.5; 2973 -2.7; 3270 -1.9; 3597 -1.2; 3957 -0.7; 4353 -0.0; 4788 1.0; 5267 2.7; 5793 5.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.0; 16529 0.0
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.3  | 6.4 dB  |
| Peaking | 843 Hz   | 0.74 | 2.3 dB  |
| Peaking | 1877 Hz  | 0.71 | -4.6 dB |
| Peaking | 6020 Hz  | 3.2  | 6.7 dB  |
| Peaking | 15045 Hz | 6.12 | -2.0 dB |
| Peaking | 157 Hz   | 3.87 | -0.3 dB |
| Peaking | 2674 Hz  | 3.66 | -1.3 dB |
| Peaking | 3015 Hz  | 1.11 | 0.6 dB  |
| Peaking | 7953 Hz  | 5.43 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20Research%20ER4SR/Etymotic%20Research%20ER4SR.png)