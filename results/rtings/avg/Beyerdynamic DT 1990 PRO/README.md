# Beyerdynamic DT 1990 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 21 -0.8; 23 -0.9; 25 -0.9; 28 -1.1; 31 -1.2; 34 -1.2; 37 -1.3; 41 -1.3; 45 -1.4; 49 -1.4; 54 -1.5; 60 -1.7; 66 -2.0; 72 -2.2; 79 -2.5; 87 -2.9; 96 -3.3; 106 -3.7; 116 -4.2; 128 -4.5; 141 -4.8; 155 -5.0; 170 -5.1; 187 -5.1; 206 -4.9; 227 -4.8; 249 -4.6; 274 -4.5; 302 -4.4; 332 -4.2; 365 -4.0; 402 -3.9; 442 -3.7; 486 -3.4; 535 -3.0; 588 -2.6; 647 -2.2; 712 -1.7; 783 -1.3; 861 -0.8; 947 -0.3; 1042 0.2; 1146 0.2; 1261 -0.0; 1387 -0.2; 1526 -0.5; 1678 -0.8; 1846 -1.1; 2031 -1.0; 2234 -0.3; 2457 -0.3; 2703 -0.5; 2973 -0.9; 3270 -1.9; 3597 -2.5; 3957 -2.0; 4353 -1.0; 4788 -1.8; 5267 -2.1; 5793 -2.7; 6373 -6.0; 7010 -9.1; 7711 -11.2; 8482 -12.5; 9330 -10.5; 10263 -6.4; 11289 -5.4; 12418 -6.3; 13660 -5.9; 15026 -4.7; 16529 -4.6; 18182 -6.9; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1990 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1990 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.09 | -0.5 dB  |
| Peaking | 209 Hz   | 0.47 | -4.8 dB  |
| Peaking | 3500 Hz  | 5.5  | -1.4 dB  |
| Peaking | 8274 Hz  | 2    | -11.8 dB |
| Peaking | 21628 Hz | 0.3  | -9.8 dB  |
| Peaking | 1078 Hz  | 3.97 | 1.2 dB   |
| Peaking | 5987 Hz  | 2.73 | 1.8 dB   |
| Peaking | 6683 Hz  | 5.39 | -2.6 dB  |
| Peaking | 13061 Hz | 4.21 | -2.2 dB  |
| Peaking | 16366 Hz | 3.84 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%201990%20PRO/Beyerdynamic%20DT%201990%20PRO.png)