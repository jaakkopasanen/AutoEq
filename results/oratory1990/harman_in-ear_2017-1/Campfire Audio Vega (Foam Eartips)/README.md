# Campfire Audio Vega (Foam Eartips)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.0; 23 -7.1; 25 -7.2; 28 -7.3; 31 -7.3; 34 -7.3; 37 -7.3; 41 -7.3; 45 -7.3; 49 -7.4; 54 -7.4; 60 -7.6; 66 -7.7; 72 -7.8; 79 -8.0; 87 -8.2; 96 -8.3; 106 -8.4; 116 -8.5; 128 -8.4; 141 -8.3; 155 -8.2; 170 -7.9; 187 -7.6; 206 -7.2; 227 -6.8; 249 -6.3; 274 -5.8; 302 -5.3; 332 -4.6; 365 -3.9; 402 -3.4; 442 -2.8; 486 -2.3; 535 -1.7; 588 -1.2; 647 -0.7; 712 -0.2; 783 0.1; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.2; 1526 0.1; 1678 0.5; 1846 1.3; 2031 2.8; 2234 4.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.0; 5267 1.5; 5793 0.2; 6373 -0.8; 7010 -0.8; 7711 -3.0; 8482 -6.1; 9330 -7.3; 10263 -7.3; 11289 -4.9; 12418 -0.7; 13660 -3.7; 15026 -12.0; 16529 -13.1; 18182 -6.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega (Foam Eartips) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega (Foam Eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.26 | -7.0 dB  |
| Peaking | 138 Hz   | 0.83 | -5.0 dB  |
| Peaking | 276 Hz   | 1.36 | -3.0 dB  |
| Peaking | 16050 Hz | 1.62 | -14.3 dB |
| Peaking | 24000 Hz | 2.12 | -10.3 dB |
| Peaking | 1536 Hz  | 1.36 | -3.7 dB  |
| Peaking | 3225 Hz  | 0.62 | 7.9 dB   |
| Peaking | 6107 Hz  | 4.53 | -2.0 dB  |
| Peaking | 9574 Hz  | 1.43 | -8.5 dB  |
| Peaking | 12762 Hz | 3.49 | 7.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Vega%20(Foam%20Eartips)/Campfire%20Audio%20Vega%20(Foam%20Eartips).png)