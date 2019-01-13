# Logitech G533
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -3.5; 23 -3.7; 25 -3.9; 28 -4.2; 31 -4.4; 34 -4.4; 37 -4.4; 41 -4.2; 45 -4.1; 49 -4.0; 54 -3.9; 60 -3.9; 66 -4.0; 72 -4.0; 79 -4.1; 87 -4.3; 96 -4.5; 106 -4.7; 116 -4.8; 128 -4.8; 141 -4.7; 155 -4.7; 170 -4.6; 187 -4.5; 206 -4.2; 227 -4.0; 249 -4.0; 274 -4.3; 302 -4.7; 332 -4.7; 365 -4.2; 402 -3.4; 442 -2.8; 486 -2.4; 535 -1.7; 588 -1.1; 647 -0.8; 712 -0.3; 783 0.7; 861 1.1; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -0.1; 1387 1.1; 1526 2.2; 1678 1.6; 1846 0.6; 2031 -0.2; 2234 -0.0; 2457 0.5; 2703 -2.5; 2973 -2.2; 3270 -1.7; 3597 -2.8; 3957 -3.8; 4353 -4.5; 4788 -2.5; 5267 -0.7; 5793 -1.1; 6373 -3.2; 7010 -3.0; 7711 -3.4; 8482 -6.7; 9330 -6.3; 10263 -1.0; 11289 -0.4; 12418 -5.1; 13660 -7.5; 15026 -5.5; 16529 -5.5; 18182 -10.0; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G533 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G533 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.38 | -3.9 dB  |
| Peaking | 146 Hz   | 0.84 | -3.6 dB  |
| Peaking | 334 Hz   | 1.84 | -3.5 dB  |
| Peaking | 7444 Hz  | 0.58 | -3.0 dB  |
| Peaking | 20243 Hz | 0.78 | -15.3 dB |
| Peaking | 1579 Hz  | 3.42 | 2.7 dB   |
| Peaking | 4391 Hz  | 2.47 | -3.9 dB  |
| Peaking | 5262 Hz  | 3    | 4.2 dB   |
| Peaking | 8920 Hz  | 5.91 | -4.4 dB  |
| Peaking | 10767 Hz | 6.43 | 5.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G533/Logitech%20G533.png)