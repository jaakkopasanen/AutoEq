# Beyerdynamic DT 880 32 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 0.0; 23 4.7; 25 4.2; 28 3.7; 31 3.3; 34 2.9; 37 2.6; 41 2.3; 45 1.9; 49 1.5; 54 1.1; 60 0.7; 66 0.7; 72 1.0; 79 -0.0; 87 -0.9; 96 -1.3; 106 -1.7; 116 -2.0; 128 -2.4; 141 -2.7; 155 -2.8; 170 -3.1; 187 -3.3; 206 -3.3; 227 -3.0; 249 -3.0; 274 -3.0; 302 -2.8; 332 -2.7; 365 -2.3; 402 -1.8; 442 -1.6; 486 -1.7; 535 -1.5; 588 -1.1; 647 -0.6; 712 -0.4; 783 -0.2; 861 -0.1; 947 0.1; 1042 0.1; 1146 0.5; 1261 0.9; 1387 0.7; 1526 0.0; 1678 -0.6; 1846 -1.0; 2031 -1.4; 2234 -1.1; 2457 -0.2; 2703 0.0; 2973 -0.3; 3270 -1.1; 3597 -1.7; 3957 -2.1; 4353 -2.4; 4788 -1.9; 5267 -3.2; 5793 -6.7; 6373 -6.7; 7010 -5.3; 7711 -7.0; 8482 -9.6; 9330 -9.1; 10263 -3.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.9; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.31 | 6.2 dB  |
| Peaking | 198 Hz   | 0.62 | -3.5 dB |
| Peaking | 6151 Hz  | 2.29 | -5.9 dB |
| Peaking | 8819 Hz  | 3.91 | -9.7 dB |
| Peaking | 20677 Hz | 2.15 | -7.2 dB |
| Peaking | 1264 Hz  | 2.5  | 1.2 dB  |
| Peaking | 1959 Hz  | 4.43 | -1.3 dB |
| Peaking | 4668 Hz  | 2.16 | -1.5 dB |
| Peaking | 4987 Hz  | 6.65 | 2.9 dB  |
| Peaking | 11492 Hz | 4.71 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)