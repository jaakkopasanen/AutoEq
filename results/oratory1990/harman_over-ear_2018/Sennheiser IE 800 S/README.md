# Sennheiser IE 800 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.8; 28 1.8; 31 1.8; 34 1.7; 37 1.7; 41 1.6; 45 1.4; 49 1.3; 54 1.2; 60 0.9; 66 0.5; 72 0.2; 79 -0.0; 87 -0.4; 96 -1.0; 106 -1.5; 116 -1.9; 128 -2.5; 141 -2.9; 155 -3.0; 170 -2.9; 187 -2.7; 206 -2.3; 227 -2.8; 249 -3.8; 274 -3.1; 302 -2.2; 332 -1.4; 365 -1.0; 402 -0.6; 442 -0.1; 486 0.4; 535 0.9; 588 1.1; 647 1.2; 712 1.3; 783 1.3; 861 1.0; 947 0.4; 1042 -0.3; 1146 -0.7; 1261 -0.7; 1387 -0.4; 1526 -0.3; 1678 0.3; 1846 1.6; 2031 3.1; 2234 4.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.5; 5267 1.1; 5793 0.5; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -1.2; 13660 -5.2; 15026 -6.9; 16529 -5.1; 18182 -3.1; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.54 | 2.0 dB   |
| Peaking | 177 Hz   | 0.88 | -3.5 dB  |
| Peaking | 3368 Hz  | 1.12 | 7.0 dB   |
| Peaking | 12758 Hz | 0.72 | 12.5 dB  |
| Peaking | 14390 Hz | 0.77 | -17.7 dB |
| Peaking | 716 Hz   | 0.93 | 6.0 dB   |
| Peaking | 918 Hz   | 0.53 | -4.9 dB  |
| Peaking | 2331 Hz  | 3.04 | 3.0 dB   |
| Peaking | 5587 Hz  | 9.18 | -3.2 dB  |
| Peaking | 6473 Hz  | 9.61 | 4.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20IE%20800%20S/Sennheiser%20IE%20800%20S.png)