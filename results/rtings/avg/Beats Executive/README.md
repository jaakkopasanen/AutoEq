# Beats Executive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 4.5; 31 2.5; 34 0.8; 37 -0.6; 41 -2.3; 45 -3.6; 49 -4.8; 54 -6.1; 60 -7.3; 66 -8.4; 72 -9.2; 79 -10.1; 87 -11.0; 96 -11.8; 106 -12.5; 116 -13.1; 128 -13.6; 141 -13.9; 155 -14.0; 170 -14.0; 187 -13.7; 206 -13.2; 227 -12.4; 249 -11.3; 274 -9.8; 302 -8.0; 332 -6.0; 365 -3.8; 402 -2.1; 442 -1.4; 486 -1.8; 535 -1.5; 588 -1.2; 647 -1.2; 712 -1.1; 783 -0.5; 861 0.8; 947 0.4; 1042 -0.4; 1146 -1.6; 1261 -1.8; 1387 -3.5; 1526 -4.6; 1678 -5.3; 1846 -6.9; 2031 -7.9; 2234 -8.4; 2457 -8.6; 2703 -8.8; 2973 -9.9; 3270 -13.5; 3597 -10.5; 3957 -4.7; 4353 -5.8; 4788 -9.1; 5267 -6.4; 5793 -4.9; 6373 -5.6; 7010 -5.2; 7711 -7.4; 8482 -8.3; 9330 -8.2; 10263 -8.1; 11289 -6.7; 12418 -6.1; 13660 -8.7; 15026 -12.2; 16529 -11.3; 18182 -7.0; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Executive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Executive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 104 Hz   | 0.9  | -10.9 dB |
| Peaking | 204 Hz   | 1.33 | -9.9 dB  |
| Peaking | 2988 Hz  | 1.04 | -10.6 dB |
| Peaking | 8796 Hz  | 1.85 | -5.3 dB  |
| Peaking | 16000 Hz | 1.01 | -11.8 dB |
| Peaking | 23 Hz    | 1.37 | 7.4 dB   |
| Peaking | 54 Hz    | 1.77 | -2.5 dB  |
| Peaking | 948 Hz   | 1.52 | 2.6 dB   |
| Peaking | 1853 Hz  | 1.14 | -2.0 dB  |
| Peaking | 2679 Hz  | 5.82 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Executive/Beats%20Executive.png)