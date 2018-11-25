# Beyerdynamic DT 880 32 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.8; 28 5.6; 31 5.3; 34 5.2; 37 5.1; 41 4.9; 45 4.8; 49 4.7; 54 4.5; 60 4.3; 66 3.9; 72 3.6; 79 3.1; 87 2.6; 96 2.1; 106 1.6; 116 1.1; 128 0.7; 141 0.3; 155 0.0; 170 -0.2; 187 -0.3; 206 -0.3; 227 -0.3; 249 -0.3; 274 -0.3; 302 -0.4; 332 -0.4; 365 -0.4; 402 -0.7; 442 -0.9; 486 -0.7; 535 -0.6; 588 -0.7; 647 -0.6; 712 -0.4; 783 -0.5; 861 -0.3; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.5; 1387 0.5; 1526 0.3; 1678 -0.7; 1846 -1.8; 2031 -2.3; 2234 -2.3; 2457 -1.8; 2703 -2.0; 2973 -1.8; 3270 -1.0; 3597 0.7; 3957 1.7; 4353 1.6; 4788 2.2; 5267 1.6; 5793 -2.3; 6373 -4.3; 7010 -2.8; 7711 -4.9; 8482 -9.2; 9330 -10.7; 10263 -8.3; 11289 -4.9; 12418 -2.5; 13660 -2.2; 15026 -3.2; 16529 -4.7; 18182 -6.5; 20000 -6.6
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
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.78 | 5.7 dB   |
| Peaking | 61 Hz    | 1.4  | 2.9 dB   |
| Peaking | 2197 Hz  | 3.27 | -2.6 dB  |
| Peaking | 9236 Hz  | 2.66 | -11.1 dB |
| Peaking | 18941 Hz | 0.99 | -7.1 dB  |
| Peaking | 774 Hz   | 0.28 | -0.8 dB  |
| Peaking | 1258 Hz  | 1.84 | 1.6 dB   |
| Peaking | 3017 Hz  | 4.85 | -1.7 dB  |
| Peaking | 4861 Hz  | 1.8  | 4.0 dB   |
| Peaking | 6076 Hz  | 4.91 | -4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)