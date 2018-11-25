# Beyerdynamic DT 880 32 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.8; 28 5.6; 31 5.3; 34 5.2; 37 5.1; 41 4.9; 45 4.8; 49 4.7; 54 4.5; 60 4.3; 66 3.9; 72 3.6; 79 3.1; 87 2.6; 96 2.1; 106 1.6; 116 1.1; 128 0.7; 141 0.3; 155 0.0; 170 -0.2; 187 -0.3; 206 -0.3; 227 -0.3; 249 -0.3; 274 -0.3; 302 -0.4; 332 -0.4; 365 -0.4; 402 -0.7; 442 -0.9; 486 -0.7; 535 -0.6; 588 -0.7; 647 -0.6; 712 -0.4; 783 -0.5; 861 -0.3; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.5; 1387 0.5; 1526 0.3; 1678 -0.7; 1846 -1.8; 2031 -2.3; 2234 -2.3; 2457 -1.8; 2703 -2.2; 2973 -2.3; 3270 -1.7; 3597 -0.4; 3957 0.5; 4353 0.3; 4788 0.4; 5267 -0.9; 5793 -4.8; 6373 -5.6; 7010 -3.5; 7711 -5.3; 8482 -8.3; 9330 -8.1; 10263 -6.1; 11289 -5.7; 12418 -5.8; 13660 -5.5; 15026 -5.8; 16529 -7.8; 18182 -10.8; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.77 | 5.7 dB   |
| Peaking | 61 Hz    | 1.4  | 2.9 dB   |
| Peaking | 2286 Hz  | 2.53 | -2.3 dB  |
| Peaking | 8834 Hz  | 1.65 | -6.7 dB  |
| Peaking | 19625 Hz | 0.62 | -12.3 dB |
| Peaking | 1265 Hz  | 1.79 | 1.7 dB   |
| Peaking | 1906 Hz  | 0.12 | -1.0 dB  |
| Peaking | 3107 Hz  | 5.36 | -1.8 dB  |
| Peaking | 5197 Hz  | 1.07 | 3.8 dB   |
| Peaking | 5975 Hz  | 4.88 | -5.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)